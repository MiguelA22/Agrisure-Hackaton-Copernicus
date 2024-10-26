import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv, find_dotenv
from formateo import formato_resp_llm
from langchain_together import Together

# Load environment variables
load_dotenv(find_dotenv())
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Configure the Anthropic LLM
llm = Together(
    model="meta-llama/Llama-3-70b-chat-hf",  # Free model
    together_api_key = TOGETHER_API_KEY,  # Explicitly passing API key
    temperature=0.7  # Added temperature for controlled randomness
)

# Create template for the agricultural report prompt
template = """
Genera un informe sobre el rendimiento agrícola basado en las siguientes métricas y que se cultiva {rubro}:
- NDVI (Índice de vegetación): {ndvi_mean}
- EVI (Índice mejorado de vegetación): {evi_mean}
- NDMI (Índice de humedad de la vegetación): {ndmi_mean}
- NDWI (Índice de agua): {ndwi_mean}
- Barren Soil (Suelo estéril): {barren_mean}

Indica el estado general del terreno, la salud de los cultivos y recomendaciones para mejorar.
"""

# Create the LangChain prompt
prompt = PromptTemplate(
    input_variables=["ndvi_mean", "evi_mean", "ndmi_mean", "ndwi_mean", "barren_mean", "rubro"],
    template=template
)

# Create the LangChain chain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Generate the report based on the data
def generar_informe_agri(data, rubro):  # Fixed typo in function name
    try:
        # Format the data
        ndvi_mean, evi_mean, ndmi_mean, ndwi_mean, barren_mean = formato_resp_llm(data)
        
        # Generate the report
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