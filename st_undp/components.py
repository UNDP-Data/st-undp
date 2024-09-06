"""
Static HTML components in UNDP style.
"""

import streamlit as st

__all__ = ["stats_card"]


def stats_card(value: int | float | str, title: str, text: str = "") -> None:
    """
    [Stats card](https://design.undp.org/?path=/docs/components-ui-components-cards-stats-card--docs) component.

    Parameters
    ----------
    value : int | float | str
        Value to be displayed, typically a number, percent etc.
    title : str
        Title to be displayed below the number.
    text : str
        Additional smaller text to be displayed below the title.

    Returns
    -------
    None.
    """
    body = f"""
        <div class='stat-card-smaller'>
            <h3>{value}</h3>
            <h4>{title}</h4>
            <p>{text}</p>
        </div>
    """
    st.html(body)
