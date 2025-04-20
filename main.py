import streamlit as st
from langchain.llms import HuggingfaceHub
import os

hf_token=os.getenv('HF_TOKEN') 

repo_id="gpt2"
llm=HuggingfaceHub(repo_id=repo_id,huggingfaceHub_api_token=hf_token,model_kwargs={"max_length":128,"temperature":0.7})

st.title("Chat with GPT-2")
st.write("the chatbot is powered by GPT-2 model hosted on hugging face")

user_input=st.text_input("you:","type your msg here")
if st.button("Send"):
    if user_input:
        try:
            response=llm(user_input)
            st.write(f"Bot:{response}")
        except Exception as e:
            st.error(f"Error:{e}")
    else:
        st.write("plzz enter a  msg ")            
