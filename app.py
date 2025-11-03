import os
from google import genai
import streamlit as st 

# --- 1. CONFIGURACIÓN Y MEMORIA (STATE) ---

# Inicializa el cliente usando la clave SECRETA de Streamlit
# (¡Recuerda que esta clave se lee del archivo .streamlit/secrets.toml!)
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 2. La personalidad de BYNUX-AI (System Prompt)
sistema_bynux = """
Eres BYNUX-AI, un asistente experto en proyectos maker que usa emojis y la palabra 'bro'. 
Tu objetivo es motivar al usuario a crear con materiales reciclados y debes recordar el contexto de la conversación.
"""

# Inicializa la sesión de chat SÓLO si no existe en la memoria de la app.
if "chat_session" not in st.session_state:
    st.session_state["chat_session"] = client.chats.create(
        model='gemini-2.5-flash',
        # ESTA SINTAXIS FUNCIONA SIEMPRE y corrige el TypeError
        config={"system_instruction": sistema_bynux} 
    )

# --- 3. DIBUJAR LA PÁGINA WEB ---

st.title("🤖 BYNUX-AI: Asistente Maker con Memoria")

# Mostrar el historial de la conversación
# Se usa un try/except para evitar errores si el historial no carga bien
try:
    for message in st.session_state.chat_session.get_messages():
        with st.chat_message(message.role):
            st.markdown(message.text)
except Exception:
    pass # Si hay un error, ignóralo para que la app no se rompa

# Caja de texto para la pregunta (la entrada del usuario)
pregunta = st.chat_input("Dile a Bynux tus materiales, bro...") 

if pregunta: 
    # Muestra la pregunta del usuario inmediatamente
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    # Envía el mensaje a la IA y usa la sesión para mantener el historial
    with st.spinner("Bynux AI está pensando..."): # Muestra que está cargando
        response = st.session_state.chat_session.send_message(pregunta)

    # Muestra la respuesta de la IA
    with st.chat_message("model"):
        st.markdown(response.text)
