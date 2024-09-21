"""
Styles and components for enhancing the look of Streamlit apps at UNDP.
"""

from io import BytesIO

import streamlit as st

from .components import *
from .utils import read_file


def apply_style(title: str = "UNDP") -> None:
    """
    Apply the styling based on UNDP Design System, including
    CSS rules and favicon.


    Parameters
    ----------
    title : str, default="UNDP"
        The page title, shown in the browser tab.

    Returns
    -------
    None
    """
    image = read_file("images/favicon.ico", "rb")
    st.set_page_config(
        page_title=title,
        page_icon=BytesIO(image),
        layout="wide",
        initial_sidebar_state="auto",
    )
    css = read_file("main.scss")
    body = f"<style>{css}</style>"
    st.html(body)
