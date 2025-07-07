import streamlit as st
import base64
from datetime import datetime

st.set_page_config(page_title="Conversor Base64", layout="centered")
# st.title("🔁 Conversor Base64 ↔️ Arquivos")
st.title("Conversor Base64 <-> Arquivos")

# Opções de conversão
opcao = st.selectbox("Escolha a conversão:", [
    "Base64 → PDF", "PDF → Base64",
    "Base64 → PNG", "PNG → Base64",
    "Base64 → DOCX", "DOCX → Base64"
])

arquivo = st.file_uploader("Selecione o arquivo", type=["txt", "pdf", "png", "docx"])

if arquivo and st.button("Converter"):
    nome_base = arquivo.name.rsplit('.', 1)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        if "→ Base64" in opcao:
            # Arquivo para Base64
            binario = arquivo.read()
            base64_data = base64.b64encode(binario).decode("utf-8")
            st.download_button(
                label="📥 Baixar Base64",
                data=base64_data,
                file_name=f"{nome_base}_{timestamp}_base64.txt"
            )
        else:
            # Base64 para Arquivo
            base64_texto = arquivo.read().decode("utf-8")
            binario = base64.b64decode(base64_texto)
            extensao = opcao.split("→")[-1].strip().lower()
            st.download_button(
                label=f"📥 Baixar {extensao.upper()}",
                data=binario,
                file_name=f"{nome_base}_{timestamp}.{extensao}"
            )
    except Exception as e:
        st.error(f"Erro na conversão: {e}")