import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello World!')
st.snow()

st.title('title string`<h1>`')
st.header('大見出し`<h2>`')
st.subheader(
    body='中見出し`<h3>`',
    anchor='title',
    help='`<h3>`あるいは`###`に相当するStreamlitコマンド',
    divider=True
)

st.caption('キャプション`<caption>`')

st.text('''
        Lorem ipsum dolor sit amet, ・・・.
        ''')

st.code('''
        import streamlit as st
         st.snow()
         ''')

