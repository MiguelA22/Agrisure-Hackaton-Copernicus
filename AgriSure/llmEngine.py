import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
from formateo import formato_resp_llm
from langchain_together import Together

# Cargar variables del token
load_dotenv(find_dotenv())
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Conffigurar modelo de Together
llm = Together(
    model="meta-llama/Llama-3-70b-chat-hf",  
    together_api_key = TOGETHER_API_KEY, 
    temperature=0.7  
)

# Crear template para el LLM
template = """
Genera un informe sobre el rendimiento agrícola basado en las siguientes métricas y que se cultiva {rubro}:
- NDVI (Índice de vegetación): {ndvi_mean}
- EVI (Índice mejorado de vegetación): {evi_mean}
- NDMI (Índice de humedad de la vegetación): {ndmi_mean}
- NDWI (Índice de agua): {ndwi_mean}
- Barren Soil (Suelo estéril): {barren_mean}

Indica el estado general del terreno, la salud de los cultivos y recomendaciones para mejorar.
"""

# Crear el prompt
prompt = PromptTemplate(
    input_variables=["ndvi_mean", "evi_mean", "ndmi_mean", "ndwi_mean", "barren_mean", "rubro"],
    template=template
)

# Crear chain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Generar el reporte de agricultura
def generar_informe_agri(data, rubro):  
    try:
        # Obtener coordenadas formateadas del poligono 
        ndvi_mean, evi_mean, ndmi_mean, ndwi_mean, barren_mean = formato_resp_llm(data)
        
        # Generar reporte
        informe = llm_chain.run({
            "ndvi_mean": ndvi_mean,
            "evi_mean": evi_mean,
            "ndmi_mean": ndmi_mean,
            "ndwi_mean": ndwi_mean,
            "barren_mean": barren_mean,
            "rubro": rubro
        })
        
        return informe
    
    except Exception as e:
        print(f"Error generando el informe: {str(e)}")
        return None
