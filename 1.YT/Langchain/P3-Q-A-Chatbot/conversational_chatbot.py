## Conversational Q&A Chatbot


### Example to test
'''
> Do you know my name 
> Please remembermy name as lucky rathod 
> Capital of my name
> Do you know my name

'''

### We will store System,Human message in session so that it remembers the context

## Streamlit will be used to remember the context 
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os

## Streamlit UI 
st.set_page_config(page_title="Conversational AI Chatbot")
st.header("Hey , Lets Chat ")

chat = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),temperature=0.5)

if 'flowmessages' not in st.session_state:
    ## If it is not present in session we will give system message 
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI Assistant')
    ]

def get_chatmodel_response(question):
    ## Storing the question in Human Message
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input('Input: ',key='input')
response = get_chatmodel_response(input)

submit = st.button('Ask the question')

## If Ask button is clicker 
if submit :
    st.subheader('The Response is')
    st.write(response)



