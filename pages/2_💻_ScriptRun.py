import streamlit as st
from pathlib import Path
import subprocess

st.set_page_config(page_title="Main work", page_icon="💻")


def create_packs():
    create_pack_script_fn = Path(__file__).parent.parent / "level_packs" / "create_pack.py"
    result = subprocess.run(["/home/ubuntu/levelpack-UI/pypy/bin/pypy", str(create_pack_script_fn)],
                            capture_output=True)
    for line in result.stdout.decode().splitlines():
        st.write(line)


def run_button():
    st.button('Run script', on_click=create_packs)


run_button()

hide_streamlit_style = """
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
