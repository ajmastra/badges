import streamlit as st
from pass_gen import *

# header container
with st.container():
    
    st.title("🧮 Password Generator")
    st.write("A simple yet effective way to generate strong passwords.")
    
# generator container
with st.container():
    st.write("---")


    # assign the desired password length to the number chosen with the slider
    password_length = st.slider("Choose your password length", min_value = 10, 
                                            max_value = 100, value = 50, step=1)

    # if the generate button is pressed
    if st.button("Generate a Password"):
        #  call the generate_password function and assign it to the 
        #                                                      variable password
        password = generate_password(password_length)
        # display the generated password
        st.write("Generated Password:")
        st.text(password)
