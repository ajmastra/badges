import streamlit as st
import pyshorteners
import validators

# initialize the shortener
s = pyshorteners.Shortener()

# header container
with st.container():
    
    # title and sub header
    st.title("🔗 URL Shortener")
    st.write("A simple way to shorten URLs.")
    
# url gen container
with st.container():
    st.write("---")

    # provide a text input for users to place their url
    user_url = st.text_input("Enter your URL:")

    # if the generate button is pressed
    if st.button("Generate shortened URL"):

        # check for valid url
        if validators.url(user_url):

            # if valid, shorten and display
            shortened_url = s.tinyurl.short(user_url)
            st.write("Shortened URL:  \n" + shortened_url)
        else:
            # otherwise ask user for valid URL
            st.write("Please enter a valid URL.")
        
        
