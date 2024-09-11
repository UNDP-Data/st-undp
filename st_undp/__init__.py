"""
Styles and components for enhancing the look of Streamlit apps at UNDP.
"""

from io import BytesIO

import streamlit as st

from .components import *
from .utils import read_file


def apply_style():
    """
    Apply the CSS rules based on [UNDP Design System](https://design.undp.org).
    """
    css = read_file("main.scss")
    body = f"<style>{css}</style>"
    st.html(body)


def set_page_config(title: str, menu_items: dict):
    image = read_file(f"images/favicon.ico", "rb")
    st.set_page_config(
        page_title=title,
        page_icon=BytesIO(image),
        layout="wide",
        initial_sidebar_state="auto",
        menu_items=menu_items,
    )
