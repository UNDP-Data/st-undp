"""
A simple Streamlit application testing and showcasing the package.
"""

import streamlit as st

import st_undp

OPTIONS = list("ABCDE")

st.set_page_config(
    page_title="st-undp App",
    page_icon=":flag-un:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/undp-data/st-undp",
        "Report a Bug": "https://github.com/undp-data/st-undp/issues",
        "About": None,
    },
)

st_undp.apply_style()

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Regular text.")

tab1, tab2, tab3 = st.tabs(["Buttons", "Forms", "Alerts"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        if clicked := st.button("Button (primary)", type="primary"):
            st.write(f"Clicked: {clicked}")
    with col2:
        if clicked := st.button("Button (secondary)", type="secondary"):
            st.write(f"Clicked: {clicked}")
with tab2:
    with st.form("form"):
        st.radio("Radio", OPTIONS, horizontal=True)
        st.number_input("Number input")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Checkbox")
            st.selectbox("Selectbox", OPTIONS)
            st.select_slider("Slider", OPTIONS)
            st.date_input("Date input")
            st.text_input("Text input (default)", type="default")
        with col2:
            st.toggle("Toggle")
            st.multiselect("Multiselect", OPTIONS)
            st.slider("Slider")
            st.time_input("Time input")
            st.text_input("Text input (password)", type="password")
        st.text_area("Text area")
        st.color_picker("Colour picker")
        st.file_uploader("File uploader")

        submitted = st.form_submit_button("Form submit button")
        if submitted:
            st.json(st.session_state)

with tab3:
    st.success("Success")
    st.info("Info")
    st.warning("Warning")
    st.error("Error")
