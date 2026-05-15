import streamlit as st
import requests


st.set_page_config(
    page_title="RAG Assistant ",
    page_icon="🤖",
    layout="wide"
)



if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:

    st.header("Configuración")
    st.write("RAG Assistant usando:")
    st.write("-Fast API ⚡")
    st.write("-ChromaDB 📚")
    st.write("-Ollama ⚙️")

    st.divider()

    if st.button("Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()


st.markdown(
    """
    <h1 style='
        font-size:50px;
        margin-top:-60px;
        margin-bottom:10px;
    '>
        RAG Assistant 🤖 
    </h1>    
    """,
    unsafe_allow_html=True)

st.caption("RAG Assistant bancario BCP")

st.markdown(
    """
    <p style='
        font-size:25px;
        margin-bottom:5px;
    '>
        Haz una pregunta:
    </p>
    """,
    unsafe_allow_html=True
)



question = st.text_input(
    "",
    label_visibility="collapsed"
)



if st.button("Enviar") and question.strip():

    with st.spinner("Consultando documentos y generando respuesta..."):

        try:

            response = requests.post(
                "http://rag-api:8000/ask",
                json={"query": question},
                timeout=300
            )

            response.raise_for_status()
            data = response.json()
            answer = data["answer"]
            chunks = data["retrieved_chunks"]

        except requests.exceptions.ConnectionError:
            st.error("No se pudo conectar con el backend FastAPI.")
            st.stop()

        except requests.exceptions.Timeout:
            st.error("El backend tardó demasiado en responder.")
            st.stop()

        except Exception as e:
            st.error(f"Error inesperado: {e}")
            st.stop()


    # Guardar historial
    st.session_state.chat_history.append({
        "question": question,
        "answer": answer,
        "chunks": chunks
    })



for chat in reversed(st.session_state.chat_history):

    st.markdown(
        """
        <div style='margin-top:30px'></div>
        """,
        unsafe_allow_html=True
    )

 
    #Usuario
    with st.chat_message("user"):

        st.write(chat["question"])
 
  
    #Asistente IA
    with st.chat_message("assistant"):

        st.write(chat["answer"])

        with st.expander("Chunks recuperados"):

            for chunk in chat["chunks"]:
                st.write(chunk)
                st.divider()