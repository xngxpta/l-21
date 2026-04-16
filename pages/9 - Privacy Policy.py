import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer
# Function to read the content of a markdown file
import base64
import os


direc = os.getcwd()

# Specify the path to your markdown file
url_stripe = "https://buy.stripe.com/9B6bJ3gWS87G97b80q0480f"
url_stripe_2 = "https://buy.stripe.com/6oUbJ35eaew4bfj0xY0480e"
st.sidebar.link_button("Access/Day!", url_stripe, type="primary",
                    disabled=False, use_container_width="True")
st.sidebar.link_button("Become a Patron!", url_stripe_2, type="primary",
                    disabled=False, use_container_width="True")
file0 = f'{direc}/pages/appdata/Privacy_Policy_Final.pdf' # Replace with your file name/path
with open(file0, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
pdf_display0 = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="350" height="250" type="application/pdf">'
st.markdown(pdf_display0, unsafe_allow_html=True)
st.write("  ---------------------------------------------------------------  ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")

