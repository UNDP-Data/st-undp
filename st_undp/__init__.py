"""
Styles and components for enhancing the look of Streamlit apps at UNDP.
"""

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
