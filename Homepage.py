import streamlit as st
from pass_gen import *


# page config
st.set_page_config(
    page_title="Password Generator",
    page_icon="💻",
    layout="wide"
)


# header container
with st.container():
    
    st.title("Password Generator")
    st.write("A simple yet effective way to generate strong passwords.")
    
# generator container
with st.container():
    st.write("---")

    password_length = st.slider("Choose your password length", min_value = 10, 
                                            max_value = 100, value = 50, step=1)

    if st.button("Generate a Password"):
        password = generate_password(password_length)
        st.text(password)

    # if a password has not been generated yet
    #if password != '':
    #    st.write({password})

# contact info container
with st.container():
    st.write("---")
    st.subheader("Hi, I am AJ 👋")
    st.write("[Checkout my Github](https://github.com/ajmastra)")

