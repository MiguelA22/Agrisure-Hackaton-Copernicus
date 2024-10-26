import requests, os
import json
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class CopernicusV2:

    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.url = "https://sh.dataspace.copernicus.eu/api/v1/statistics"
        #self.token_url = 'https://services.sentinel-hub.com/auth/realms/main/protocol/openid-connect/token'
        self.token_url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'
        self.session = self._get_oauth_session()
        self.headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    }
        self.evalscript = """
                        //VERSION=3
                        function setup() {
                        return {
                            input: [{
                            bands: [
                                "B02",
                                "B03",
                                "B04",
                                "B08",
                                "B11",
                                "dataMask"
                            ]
                            }],
                            output: [
                            {
                                id: "data",
                                bands: ["NDVI","EVI","NDMI","NDWI","BARREN"]
                            },
                            {
                                id: "dataMask",
                                bands: 1
                            }]
                        };
                        }

                        function evaluatePixel(samples) {
                            let ndvi = (samples.B08 - samples.B04) / (samples.B08+samples.B04);
                            let evi = 2.5 * (samples.B08 - samples.B04) / ((samples.B08 + 6.0 * samples.B04 - 7.5 * samples.B02) + 1);
                            let ndmi = (samples.B08 - samples.B11) / (samples.B08 + samples.B11);
                            let ndwi =  (samples.B03 - samples.B08) / (samples.B03 + samples.B08);
                            let barren = 2.5 * ((samples.B11 + samples.B04)-(samples.B08 + samples.B02))/((samples.B11 + samples.B04)+(samples.B08 + samples.B02));
                            return {
                                data: [ndvi,evi,ndmi,ndwi,barren],
                                dataMask: [samples.dataMask]
                            };
                        }

                    """
        

    def _get_oauth_session(self):
        
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url=self.token_url,
            client_id=self.client_id,
            client_secret=self.client_secret
        )
        return oauth

    
    def get_data_sta(self, coord,start_date=None, end_date = None):

        # Tomar fechas a partir del día que se introduce las coord y el día anterior
        if not start_date:
            start_date = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')
        
        # Convertir las fecha a formato ISO
        start_iso = datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
        end_iso = datetime.strptime(end_date, '%Y-%m-%d').isoformat() + 'Z'


        data = {
                    "input": {
                        "bounds": {
                        "bbox": coord
                        },
                        "data": [
                        {
                            "dataFilter": {},
                            "type": "sentinel-2-l2a"
                        }
                        ]
                    },
                    "aggregation": {
                        "timeRange": {
                        "from": start_iso,
                        "to": end_iso
                        },
                        "aggregationInterval": {
                        "of": "P10D"
                        },
                        "evalscript": "//VERSION=3\nfunction setup() {\n  return {\n    input: [{\n      bands: [\n        \"B02\",\n        \"B03\",\n        \"B04\",\n        \"B08\",\n        \"B11\",\n        \"dataMask\"\n      ]\n    }],\n    output: [\n      {\n        id: \"data\",\n        bands: [\"NDVI\",\"EVI\",\"NDMI\",\"NDWI\",\"BARREN\"]\n      },\n      {\n        id: \"dataMask\",\n        bands: 1\n      }]\n  };\n}\n\nfunction evaluatePixel(samples) {\n    let ndvi = (samples.B08 - samples.B04) / (samples.B08+samples.B04);\n    let evi = 2.5 * (samples.B08 - samples.B04) / ((samples.B08 + 6.0 * samples.B04 - 7.5 * samples.B02) + 1);\n    let ndmi = (samples.B08 - samples.B11) / (samples.B08 + samples.B11);\n    let ndwi =  (samples.B03 - samples.B08) / (samples.B03 + samples.B08);\n    let barren = 2.5 * ((samples.B11 + samples.B04)-(samples.B08 + samples.B02))/((samples.B11 + samples.B04)+(samples.B08 + samples.B02));\n    return {\n        data: [ndvi,evi,ndmi,ndwi,barren],\n        dataMask: [samples.dataMask]\n    };\n}\n"
                    },
                    "calculations": {
                        "default": {}
                    }
                }

        

        response = self.session.request("POST", url = self.url, headers=self.headers, json=data)
        sh_stattistics = response.json()
        return sh_stattistics