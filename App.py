import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar

from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('img/WhatsApp.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

pages =["Home","Project1","Project2","Project3"]

styles = {
    "nav" : {
        "background-color": "red",
        "display":"flex",
        "justify-content": "center",
    },
    "img" : {
        "position": "absolute",
        "left":"-20px",
        "font-size": "15px",
        "top":"4px",
        "width":"80px",
        "height":"80px",
    },
    "span": {
        "display":"block",
        "color":"black",
        "padding":"0.2rem 0.725rem",
        "font-size":"14px",
    },
    "active": {
        "background-color": "white",
        "color": "blue",
        "font-weight": "normal",
        "padding": "14px",
    },
}

page = navbar (pages, styles = styles)

if page =="Home":
    Home.Home().app()
elif page =="Project1":
    Project1.Project1().app()
elif page =="Project2":
    Project2.Project2().app()
elif page =="Project3":
    Project3.Project3().app()
else:
    Home.Home().app()