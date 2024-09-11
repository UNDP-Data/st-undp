"""
Static HTML components in UNDP style.
"""

import json
from typing import Literal

import streamlit as st
from jinja2 import Environment, PackageLoader

from .utils import read_file

__all__ = ["footer", "logo", "stats_card"]


env = Environment(loader=PackageLoader("st_undp"))


def logo(
    name: Literal["undp", "pnud"] = "undp",
    colour: Literal["blue", "white"] = "blue",
    title: str = r"Data Futures \A Exchange",
    link: str = "https://data.undp.org",
):
    css = f"""
    a[data-testid="stLogoLink"]::after {{
      content: "{title}";
    }}
    """
    st.html(f"<style>{css}</style>")
    image = read_file(f"images/{name}-logo-{colour}.svg", "r")
    st.logo(image=image, link=link, icon_image=image)


def footer(columns: Literal["dfx", "default"] | dict[str, dict[str, str]] = "default"):
    if isinstance(columns, str):
        data = read_file(f"data/footer-{columns}.json")
        columns = json.loads(data)
    elif isinstance(columns, dict):
        pass
    else:
        raise ValueError("Columns must one of 'dfx', 'default', or a mapping.")
    items = []
    for index, (title, pages) in enumerate(columns.items(), start=1):
        item = __footer_item(id=index, title=title, pages=pages)
        items.append(item)
    template = env.get_template("footer.html")
    body = template.render(items=items)
    st.html(body)


def __footer_item(id: int, title: str, pages: dict) -> str:
    template = env.get_template("footer-item.html")
    return template.render(id=id, title=title, pages=pages)


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
