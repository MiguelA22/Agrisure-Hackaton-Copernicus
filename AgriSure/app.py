import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_pills import pills
import formateo as ft
import json

from copernicusV2 import CopernicusV2
from llmEngine import generar_informe_agri


# Inizializar CopernicusV2 para obtener datos de Statistics API
coperV2 = CopernicusV2()



# Crear mapa central
with st.container():
    st.title("AgriSure Demo")

    mapa = folium.Map(location=[8.538, -80.7821], zoom_start=7, tiles="Esri.WorldImagery")

    # Permitir crear poligonos sobre el mapa
    folium.plugins.Draw(export=True).add_to(mapa)

    # Renderizar el mapa en streamlit
    output = st_folium(mapa, width=700, height=500)


    # Seleccionar rubros del lugar
    rubro = pills("Seleccione el rubro a asegurar",
                ["Arroz","Cebolla", "Maíz", "Tomate", "Aji", "Lechuga", "Café", "Piña", "Sandía", "Melon", "Papa", "Banano","Cítricos", "Palma aceitera"],
                ["🌾","🧅", "🌽", "🍅", "🌶️", "🥬", "☕", "🍍", "🍉", "🍈", "🥔", "🍌", "🍊", "🌴"])

with st.container():
    print()

with st.container():
    if st.button("Buscar seguro", type="primary", icon="🔍") and output and 'all_drawings' in output and output['all_drawings'] is not None:
        # Extraer coordenadas del poligono
        polygon = output['all_drawings'][0]
        coordinates = polygon['geometry']['coordinates'][0] 
        coord = ft.convertir_formato_coordenadas(output['all_drawings'])

        # Obtener data de copernicus
        data = coperV2.get_data_sta(coord)
        data_json = json.dumps(data, indent=4)

        col1, col2 = st.columns(2)

        with col1:
            st.title("Información Extraida de Copernicus")
            st.write(f"Data de copernicus: ", data)

        
        with col2:
            # Informe de para LLM prueba
            st.title("Informe de cultivos")
            st.write(generar_informe_agri(data_json,rubro))

    else:
        st.write("Seleccione las coordenadas de la zona")


