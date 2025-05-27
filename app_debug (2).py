
import streamlit as st
import os

from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="StatsCan Chatbot", layout="wide")
st.title("📊 Statistics Canada AI Chatbot (Debug Mode)")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found in environment.")
else:
    st.success("✅ OPENAI_API_KEY found and loaded.")

query = st.text_input("Ask your question:")

if query and api_key:
    try:
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, openai_api_key=api_key)


        response = llm.predict(query)
        st.markdown("### ✅ Answer")
        st.write(response)
    except Exception as e:
        st.error(f"🔥 Error occurred: {e}")
