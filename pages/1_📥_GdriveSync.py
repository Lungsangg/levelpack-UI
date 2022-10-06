import streamlit as st
from upload_to_drive import main as u
from download_from_drive import main as d


def upload():
    u()


def download():
    d()


if __name__ == "__main__":
    col1, col2 = st.columns(2)

    with col1:
        st.button('upload to gdrive', on_click=upload)

    with col2:
        st.button('download from gdrive', on_click=download)



