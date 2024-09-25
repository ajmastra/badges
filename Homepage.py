import streamlit as st
from pass_gen import *


# page config
st.set_page_config(
    page_title="Python Utilities",
    page_icon="💻",
    layout="centered"
)

# header container
with st.container():
    
    st.title("Welcome to Python Web Utilities!")
    st.write("A collection of useful tasks, automated by Python.")
    
# navigation container
with st.container():
    st.write("---")

    # link password generator
    st.page_link(
        "pages/1_🔑_Password_Generator.py", 
        label=None, 
        icon="🔑",
        use_container_width=True

    )

    # link url shortener
    st.page_link(
        "pages/2_🔗_URL_Shortener.py", 
        label=None, 
        icon="🔗",
        use_container_width=True

    )

    # link url shortener
    st.page_link(
        "pages/3_🧮_Calculator.py", 
        label=None, 
        icon="🧮",
        use_container_width=True

    )

# contact info container
with st.container():
    st.write("---")
    st.subheader("Hi, I am AJ 👋")
    st.write("[Checkout my Github](https://github.com/ajmastra)")

