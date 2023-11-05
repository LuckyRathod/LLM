## Integrate our Code with Open AI API
import os 
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
os.environ["OPENAI_API_KEY"] = openai_key

## Initialize Streamlit framework 
st.title('Langchain demo with Open AI API')
input_text = st.text_input('Search the topic you want')

## OpenAI LLMS
## temperature - How much control agent should have while providing the response.
## How much balanced ans you want is determined by temperature
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))

## In order to run streamlit applications 
## > streamlit run main.py 
