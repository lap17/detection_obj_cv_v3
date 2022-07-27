import streamlit as st
import sys
sys.path.append('mediapipe')
from detect_weapon import detect_objects
from streamlitMediapipe import mediapipe_f

def main():
    st.header("Computer Vision Demo")

    pages = {
        "Real time object detection": detect_objects,
        "Detection pipe": mediapipe_f}
    page_titles = pages.keys()

    page_title = st.sidebar.selectbox(
        "Choose the app mode",
        page_titles,
    )
    st.subheader(page_title)
    page_func = pages[page_title]
    page_func()
    
main()