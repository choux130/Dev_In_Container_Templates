import os
import sys
import streamlit as st
import pandas as pd
import requests

sys.path.append(os.path.realpath('../'))
from src.myfuns import AddTen


url = "http://api:5050/"
response = requests.get(
    url,
    headers={"Content-Type": "application/json; charset=utf-8"}
)

status_code = response.status_code
content = response.content

body = f"**Successfully get output by calling url,** {url} <br />* status_code: {status_code}, <br /> * content: {content}"


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df['first column'] = df['first column'] .apply(lambda x: AddTen(x))

st.write(body, unsafe_allow_html=True)
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

