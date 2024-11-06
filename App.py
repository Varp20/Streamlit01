import streamlit as st
from tornado.options import options

from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar, st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('img/WhatsApp.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path=os.path.join(os.path.dirname(__file__), 'img', 'WhatsApp.svg')
pages =[" ","Home","Project1","Project2","Project3"]

styles = {
    "nav" : {
        "background-color": "red",
        "display":"flex",
        "justify-content": "center",
    },
    "img" : {
        "position": "absolute",
        "font-size": "15px",
        "width":"44px",
        "height":"44px",
        "bottom":"0px",
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

page = st_navbar(pages,
    styles = styles,
    logo_path=logo_path)

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