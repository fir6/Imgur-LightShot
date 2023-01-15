# Import string and random module
import streamlit as st
import webbrowser
import string
import random
import os
import streamlit.components.v1 as components
st.title('Random Light Shot/Imgur Image')
if st.button('Click for a random Light Shot Image'):
    # Randomly choose a letter from all the ascii_letters
    a = random.choice(string.ascii_letters)
    b = random.choice(string.ascii_letters)
    num = random.randrange(1000, 9999)
    link = 'prnt.sc/'+'a'+'b'+str(num)
    webbrowser.open(link, new = 2)





    
if st.button('Click for a random Imgur image'):
    
    chars = '0123456789ABCDEFGHIJKLMNAOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    text = ''

    for i in range(5):
        if len(text) != 5:
            text += random.choice(chars)
            
    url = 'https://i.imgur.com/' + text + '.jpg'

    webbrowser.open(url, new = 0)

