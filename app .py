import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot using LLMs")
st.write("Ask anything and get AI-generated responses")

user_input = st.text_input("You:")

if st.button("Send"):
    if user_input.strip() != "":
        response = requests.post(
            "http://localhost:8000/chat",
            json={"message": user_input}
        )
        if response.status_code == 200:
            st.success("Bot:")
            st.write(response.json()["reply"])
        else:
            st.error("Error connecting to backend")
