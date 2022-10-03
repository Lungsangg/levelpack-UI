import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.write("# Welcome to Level-pack 👋")
st.subheader("User Manual 📖")

st.sidebar.success("User manual page")

st.markdown(
    """
    1. GdriveSync:
    2. Run Script:
     """
)


st.button("Change config")

