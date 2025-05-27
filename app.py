
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="StatsCan Chatbot", layout="wide")
st.title("📊 Statistics Canada AI Chatbot (Demo)")

query = st.text_input("Ask a question about Canadian statistics:")

if query:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OPENAI_API_KEY environment variable not set.")
    else:
        llm = ChatOpenAI(model="gpt-4", temperature=0.2, openai_api_key=openai_api_key)
        response = llm.predict(query)
        st.markdown("### ✅ Answer")
        st.write(response)
