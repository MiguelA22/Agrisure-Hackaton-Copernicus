import json

# Funciones para formatear json de ubicación
def convert_geojson_to_bbox(geojson):
    # Extraemos las coordenadas del polígono
    coordinates = geojson['geometry']['coordinates'][0]
    
    # Obtenemos las longitudes (X) y latitudes (Y)
    longitudes = [coord[0] for coord in coordinates]
    latitudes = [coord[1] for coord in coordinates]
    
    # Calculamos los valores extremos para el Bounding Box
    min_lon = min(longitudes)
    max_lon = max(longitudes)
    min_lat = min(latitudes)
    max_lat = max(latitudes)
    
    # Creamos el objeto BBox con CRS (Sistema de referencia de coordenadas) WGS84
    coords = [min_lon, min_lat, max_lon, max_lat]

    return coords


def convertir_formato_coordenadas(datos_entrada):
    """
    Convierte el formato de coordenadas dado al formato GeoJSON estándar
    """
    coordinates = []
    for punto in datos_entrada[0]["geometry"]["coordinates"][0]:
        coordinates.append([punto[0], punto[1]])
    
    geojson_formateado = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [coordinates]
        }
    }
    
    return convert_geojson_to_bbox(geojson_formateado)

#----------------------Funciones para formateo de JSON de respuesta a LLM------------------------

def formato_resp_llm(data):
    copernicus_data = json.loads(data)

    # Extraer las métricas relevantes
    data_bands = copernicus_data['data'][0]['outputs']['data']['bands']
    ndvi_mean = data_bands['NDVI']['stats']['mean']
    evi_mean = data_bands['EVI']['stats']['mean']
    ndmi_mean = data_bands['NDMI']['stats']['mean']
    ndwi_mean = data_bands['NDWI']['stats']['mean']
    barren_mean = data_bands['BARREN']['stats']['mean']

    return ndvi_mean, evi_mean, ndmi_mean, ndwi_mean, barren_mean