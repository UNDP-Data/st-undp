"""
   Plotly custom theme and configuration
"""

import json

import plotly.io as pio

from .utils import read_file


def load_plotly_theme():
    """
    Loads UNDP theme configuration json file
    """
    config = read_file("data/plotly-theme.json")
    return json.loads(config)


def set_plotly_theme():
    """
    Defines custom UNDP theme for Plotly charts
    """
    custom_template = load_plotly_theme()
    pio.templates["undp"] = custom_template


def apply_plotly_theme():
    """
    Applies UNDP theme for Plotly charts
    """
    pio.templates.default = "undp"
