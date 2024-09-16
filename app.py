"""
A simple Streamlit application testing and showcasing the package.
"""

import streamlit as st

import st_undp

st_undp.set_page_config(
    title="st-undp App",
    menu_items={
        "Get help": "https://github.com/undp-data/st-undp",
        "Report a Bug": "https://github.com/undp-data/st-undp/issues",
        "About": "Developed with [st-undp](https://github.com/undp-data/st-undp).",
    },
)

st_undp.apply_style()

# initialise states
if st.session_state.get("title") is None:
    st.session_state["title"] = "Data Futures Exchange"
    st.session_state["subtitle"] = "st-undp Application"
    st.session_state["logo"] = "UNDP"

# configure the header
st_undp.header(
    title=st.session_state.title,
    subtitle=st.session_state.subtitle,
    pages={
        "standard components": "./",
        "custom components": "./custom",
    },
    logo=st.session_state.logo.lower(),
)

pg = st.navigation(
    pages=[
        st.Page("pages/standard.py", url_path="/", default=True),
        st.Page("pages/custom.py", url_path="/custom"),
    ],
    position="hidden",
)
pg.run()
