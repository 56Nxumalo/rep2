import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Title Heading")

st.write("Hello, Streamlit!")

st.header("Sample Data")

data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})

st.write(data)


