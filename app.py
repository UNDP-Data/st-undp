"""
A simple Streamlit application testing and showcasing the package.
"""

import streamlit as st

import st_undp

st_undp.apply_style(title="st-undp App")

# initialise states
if st.session_state.get("title") is None:
    st.session_state["title"] = "Data Futures Exchange"
    st.session_state["subtitle"] = "st-undp Application"
    st.session_state["logo"] = "UNDP"


# define the pages
pages = [
    st.Page(
        page="pages/standard.py",
        title="standard components",
        url_path="./",  # use this pattern and not the `default` parameter
    ),
    st.Page(
        page="pages/custom.py",
        title="custom components",
        url_path="/custom",
    ),
    st.Page(
        page="pages/about.py",
        title="about",
        url_path="/about",
    ),
]


# configure the header
st_undp.header(
    title=st.session_state.title,
    subtitle=st.session_state.subtitle,
    title_href="https://data.undp.org",
    subtitle_href="./",
    pages=pages,
    logo=st.session_state.logo.lower(),
)

pg = st.navigation(pages=pages, position="hidden")
pg.run()
