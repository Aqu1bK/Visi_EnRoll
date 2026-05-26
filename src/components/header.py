import os
import streamlit as st
import base64

def get_image_base64(image_path):
    """Convert local image to base64 string"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def header_home():
    # SIMPLE RELATIVE PATH - works when running from app.py
    image_path = "src/static/visi_enroll.png"
    
    # Convert to base64
    img_base64 = get_image_base64(image_path)
    logo_url = f"data:image/png;base64,{img_base64}"
    
    # Use your EXACT HTML structure with the base64 image
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>Visi<br/>EnRoll</h1>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():
    # SIMPLE RELATIVE PATH - works when running from app.py
    image_path = "src/static/visi_enroll.png"
    
    # Convert to base64
    img_base64 = get_image_base64(image_path)
    logo_url = f"data:image/png;base64,{img_base64}"
    
    # Use your EXACT HTML structure with the base64 image
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>Visi<br/>EnRoll</h2>
        </div>   
    """, unsafe_allow_html=True)