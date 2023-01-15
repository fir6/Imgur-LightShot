import streamlit as st
import requests
import re

# Scrape a random image URL from Imgur
response = requests.get("https://imgur.com/random")
response.raise_for_status()
image_url = re.search(r'<img src="(.+?)"', response.text).group(1)

# Display the image
st.markdown(f'<img src="{image_url}" style="width:100%"/>', unsafe_allow_html=True)
