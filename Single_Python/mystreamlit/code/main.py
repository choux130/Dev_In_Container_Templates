import os
import sys
import streamlit as st
import pandas as pd

sys.path.append(os.path.realpath('../'))
from src.myfuns import AddTen

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df['first column'] = df['first column'] .apply(lambda x: AddTen(x))

st.write("Here's our first attempt at using data to create a table:")
st.write(df)