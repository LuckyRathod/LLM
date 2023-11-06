## Q&A Chabot 

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 

## Function to load openai model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name="text-davinci-003",temperature=0.6)
    response = llm(question)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header('Langchain Application')

input = st.text_input('Input: ',key='input')
response = get_openai_response(input)

submit = st.button('Ask the question')

## If Ask button is clicker 
if submit :
    st.subheader('The Response is')
    st.write(response)


