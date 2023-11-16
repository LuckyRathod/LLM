import streamlit as st
import langchain_helper 
st.title('Restaurant Name Generator')

## Picker for cuisine
cuisine = st.sidebar.selectbox('Pick a Cuisine',('Indian','Italian','Mexican','Arabic','American'))

if cuisine:
    ## Will generate RestrauntName and its Menu Item 
    response = langchain_helper.generate_restraunt_name_and_items(cuisine)
    ## strip will remove Leading and trailing white spaces
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write('** Menu Items **')
    for item in menu_items:
        st.write('-',item)