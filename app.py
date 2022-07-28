import streamlit as st
import sys
sys.path.append('mediapipe')
from detect_weapon import func_detect_weapon
from streamlitMediapipe import mediapipe_f
from detect_fire_smoke import func_detect_fire_smoke
def main():
    st.header("Computer Vision Demo")

    pages = {
        "Real time hand items detection": func_detect_weapon,
        "Detection pipe": mediapipe_f,
        "Real time fire and smoke detection": func_detect_fire_smoke
    }
    page_titles = pages.keys()

    page_title = st.sidebar.selectbox(
        "Choose the app mode",
        page_titles,
    )
    st.subheader(page_title)
    page_func = pages[page_title]
    page_func()
    
main()