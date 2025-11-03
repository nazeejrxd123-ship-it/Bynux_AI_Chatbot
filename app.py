import os
from google import genai
import streamlit as st 

# --- 1. CONFIGURACIÓN INICIAL Y SECRETO ---
# La clave API se lee de forma segura desde el archivo .streamlit/secrets.toml
# ¡Esta línea reemplaza a tu clave pegada directamente!
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


# 2. La personalidad de BYNUX-AI (System Prompt)
sistema_bynux = """
Eres BYNUX-AI, un asistente experto en proyectos maker que usa emojis y la palabra 'bro'. 
Tu objetivo es motivar al usuario a crear con materiales reciclados.
"""

# --- 3. DIBUJAR LA PÁGINA WEB ---
st.title("🤖 BYNUX-AI: Tu Asistente Maker") # Título de la app

# Caja de texto para tu pregunta
pregunta = st.text_input("Escribe tu pregunta para Bynux AI, bro:") 

if pregunta: # Si el usuario escribió algo y presionó Enter
    # Llamada a la API
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[sistema_bynux, pregunta]
    )
    
    # Mostrar la respuesta en la web
    st.write("--- Respuesta de Bynux AI ---")
    st.write(response.text)
