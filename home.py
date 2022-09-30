import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Level-pack 👋")
st.subheader("User Manual 📖")

st.sidebar.success("User manual page")

st.markdown(
    """
    1. Input data:
    2. Pipeline message:
    3. Main work:
    4. Report:
     """
)


st.button("Change config")

