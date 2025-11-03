# app.py
# El código de Bynux AI con la interfaz visual de Streamlit

# IMPORTANTE: Necesitarías instalar Streamlit, pero eso se hace después:
# !pip install streamlit

import os
from google import genai
import streamlit as st # La nueva librería para la interfaz

# --- 1. CONFIGURACIÓN INICIAL ---
# La llave API y el cliente se configuran aquí. 
# Recuerda que en la app real, NO pegas la llave aquí, sino que la pones 
# en un archivo de configuración SECRETO. 
# Por ahora, usamos el os.environ para probar:
os.environ['GEMINI_API_KEY'] = 'AIzaSyAgpopqmEGKPxR9COhyxcIbX8RNQ18fAFs'
client = genai.Client()

# 2. La personalidad de BYNUX-AI (System Prompt)
sistema_bynux = "Eres BYNUX-AI, un asistente experto en proyectos maker que usa emojis y la palabra 'bro'."
# (Aquí iría también tu base_de_conocimiento BDD)

# --- 3. DIBUJAR LA PÁGINA WEB ---
st.title("🤖 BYNUX-AI: Tu Asistente Maker") # Título de la app

pregunta = st.text_input("Escribe tu pregunta para Bynux AI, bro:") # La caja de texto

if pregunta: # Si el usuario escribió algo y presionó Enter
    # Llamada a la API
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[sistema_bynux, pregunta]
    )
    
    # Mostrar la respuesta en la web (en lugar de usar print)
    st.write("--- Respuesta de Bynux AI ---")
    st.write(response.text)
