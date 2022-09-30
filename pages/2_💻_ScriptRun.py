import streamlit as st

from level_packs import create_packs as f

st.set_page_config(page_title="Main work", page_icon="💻")


def run_button():
    st.button('Run script', on_click=f)


run_button()

hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
