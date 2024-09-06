"""
Styles and components for enhancing the look of Streamlit apps at UNDP.
"""

from importlib import resources

import streamlit as st

from .components import *


def apply_style():
    """
    Apply the CSS rules based on [UNDP Design System](https://design.undp.org).
    """
    with resources.open_text("st_undp", "style.html") as file:
        body = file.read()
    st.html(body)
