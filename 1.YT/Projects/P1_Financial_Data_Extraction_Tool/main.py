import streamlit as st
import pandas as pd 
import openai_helper

##  We will divide the screen size out of 5 
col1,col2 = st.columns([3,2])
financial_data_df = pd.DataFrame({
        "Measure":["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Value":["","","","",""]
    })

with col1:
    st.title('Data Extraction Tool')
    news_article = st.text_area("Paste your financial news article here",height=300)

    ## When button is clicked 
    if st.button('Extract'):
        financial_data_df = openai_helper.extract_financial_data(news_article)

with col2:
    ## For Alignment 
    st.markdown("<br/>" * 5 ,unsafe_allow_html=True) ## Creates 5 line of vertical space
    st.dataframe(financial_data_df,
                 column_config={
                     'Measure': st.column_config.Column(width=150),
                     'Value': st.column_config.Column(width=150)
                 },     
                 hide_index=True)
