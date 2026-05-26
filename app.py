import os
import streamlit as st
import base64


from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def get_image_base64(image_path):
    """Convert local image to base64 string"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
logo_path = "src/static/visi_enroll.png"
logo_base64 = get_image_base64(logo_path)
page_icon_data = f"data:image/png;base64,{logo_base64}"

def main():
    st.set_page_config(
        page_title='Visi-EnRoll - Making Attendance faster using AI',
        page_icon= page_icon_data
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()
