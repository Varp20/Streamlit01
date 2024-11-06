import streamlit as st
import pandas as pd
import numpy as np
from click import style
from jinja2.sandbox import unsafe


class Project1:
    def __int__(self):
        pass
    def app(self):
        st.title("Creation of DataFrame")

        def load_data(file):
            if file is not None:
                data= pd.read_csv(file)
                return data
            return None

        upload=st.file_uploader("Upload a CSV file")
        if upload is not None:
            df=load_data(upload)
            st.dataframe(df, height=400, width=600)
        else:
            st.warning("Please upload a CSV file")

        st.markdown("""<style>
                    h1{
                    color: Yellow;
                    font-size:18px;
                    text-align:center;
                   }
                    </style>""", unsafe_allow_html=True)