import streamlit as st
from streamlit_extras.colored_header import colored_header
from st_pages import add_page_title
from streamlit_extras.add_vertical_space import add_vertical_space

add_page_title(layout="wide")

colored_header(
    description="Welcome to Our Projects, Satria Data 2023!",
    label="License Plate Recognition",
    color_name="violet-70",
)

st.sidebar.success("SD2023040000171")