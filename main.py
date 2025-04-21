import streamlit as st
from langchain_community.llms import HuggingFaceHub

# Securely get the token
hf_token = st.secrets["HF_TOKEN"]

repo_id = "gpt2"
llm = HuggingFaceHub(
    repo_id=repo_id,
    huggingfacehub_api_token=hf_token,
    model_kwargs={"max_length": 128, "temperature": 0.7}
)

st.title("Chat with GPT-2")
st.write("The chatbot is powered by GPT-2 model hosted on Hugging Face")

user_input = st.text_input("You:", "Type your msg here")
if st.button("Send"):
    if user_input:
        try:
            response = llm(user_input)
            st.write(f"Bot: {response}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Please enter a message.")
