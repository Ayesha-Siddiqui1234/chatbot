import streamlit as st
from langchain_community.llms import HuggingFaceHub
import os

hf_token = os.getenv('HF_TOKEN')
repo_id = "mistralai/Mistral-7B-Instruct-v0.1"
os.environ['HUGGINGFACEHUB_API_TOKEN'] = hf_token

llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"max_length": 128, "temperature": 0.7})

st.title("Chat with GPT-2")
st.write("The chatbot is powered by GPT-2 model hosted on Hugging Face")

user_input = st.text_input("You:", "Type your message here")

if st.button("Send"):
    if user_input:
        try:
            response = llm(user_input)
            st.write(f"Bot: {response}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Please enter a message")

