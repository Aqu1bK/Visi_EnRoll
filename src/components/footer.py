import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white;">AI-Based Attendance Application</p>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    st.markdown("""
        <div style="margin-top:2rem; display:flex; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black;">AI-Based Attendance Application</p>
        </div>
    """, unsafe_allow_html=True)