"""
Static HTML components from the [UNDP Design System](https://design.undp.org).
"""

import json
from base64 import b64encode
from typing import Literal

import streamlit as st
from jinja2 import Environment, PackageLoader

from .utils import read_file

__all__ = [
    "header",
    "footer",
    "author",
    "author_card",
    "author_summary",
    "breadcrumb",
    "content_card",
    "download_card",
    "featured_card",
    "image_card",
    "stats_card",
]


env = Environment(loader=PackageLoader("st_undp"))


def header(
    title: str,
    subtitle: str,
    title_href: str | None = None,
    subtitle_href: str | None = None,
    pages: list[st.Page] | None = None,
    logo: Literal["undp", "pnud"] = "undp",
) -> None:
    """
    [Header](https://design.undp.org/?path=/docs/components-navigation-components-main-navigation-country-header--docs) component.

    Parameters
    ----------
    title : str
        Title displayed in the header.
    subtitle : str
        Subtitle displayed in the header below the title.
    title_href : str | None, optional
        URL assigned to the title.
    subtitle_href : str | None, optional
        URL assigned to the subtitle.
    pages : list[st.Page] | None, optional
        List of pages to add as navigation in the header.
    logo : Literal["undp", "pnud"], default="undp"
        One of the two versions of the logo to use.

    Returns
    -------
    None
    """
    kwargs = locals()
    # read the logo image
    image = read_file(f"images/{logo}-logo-blue.svg", "r")
    data = b64encode(image.encode("utf-8")).decode("utf-8")

    # update the variable as needed
    if kwargs["pages"]:
        kwargs["pages"] = {page.title: page.url_path for page in kwargs["pages"]}
    else:
        kwargs["pages"] = {}
    kwargs["logo"] = f"data:image/svg+xml;base64,{data}"

    template = env.get_template("header.html")
    body = template.render(**kwargs)
    st.html(body)


def footer(
    columns: Literal["dfx", "default"] | dict[str, dict[str, str]] = "default"
) -> None:
    """
    [Footer](https://design.undp.org/?path=/docs/components-ui-components-footer--docs) component.

    Parameters
    ----------
    columns : Literal["dfx", "default"] | dict[str, dict[str, str]], default="default"
        Either a literal specifying the type of the footer to use or a mapping from column titles to column items.

    Returns
    -------
    None
    """
    if isinstance(columns, str):
        data = read_file(f"data/footer-{columns}.json")
        columns = json.loads(data)
    elif isinstance(columns, dict):
        pass
    else:
        raise ValueError("Columns must one of 'dfx', 'default', or a mapping.")
    items = []
    for title, pages in columns.items():
        item = __footer_item(title=title, pages=pages)
        items.append(item)
    template = env.get_template("footer.html")
    body = template.render(items=items)
    st.html(body)


def __footer_item(title: str, pages: dict[str, str]) -> str:
    """
    Get a template for the footer item.

    Parameters
    ----------
    title : str
        Title for the column of items.
    pages : dict[str, str]
        Mapping from item names to item URLs.

    Returns
    -------
    str
        HTML template.
    """
    template = env.get_template("footer-item.html")
    return template.render(title=title, pages=pages)


def author(src: str, name: str, title: str, href: str) -> None:
    """
    [Author](https://design.undp.org/?path=/docs/components-ui-components-authors-author--docs) component.

    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    name : str
        Name of the author.
    title : str
        Title of the author, typically a position.
    href : str
        URL the component points to when clicked.

    Returns
    -------
    None
    """
    kwargs = locals()
    template = env.get_template("author.html")
    body = template.render(**kwargs)
    st.html(body)


def author_card(
    src: str,
    name: str,
    title: str,
    summary: str,
    href: str,
    link: str = "view",
    width: int = 4,
) -> None:
    """
    [Author card](https://design.undp.org/?path=/docs/components-ui-components-authors-author-card--docs) component.

    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    name : str
        Name of the author.
    title : str
        Title of the author, typically a position.
    summary : str
        Summary text displayed below the author.
    href : str
        URL the component points to when clicked.
    link : str
        Text displayed below the summary, typically "READ MORE" or similar.
    width : int, default=4
        Component width using a 12-grid scheme.

    Returns
    -------
    None
    """
    kwargs = locals()
    template = env.get_template("author-card.html")
    body = template.render(**kwargs)
    st.html(body)


def author_summary(src: str, name: str, title: str, summary: str) -> None:
    """
    [Author summary](https://design.undp.org/?path=/docs/components-ui-components-author-summary--docs) component.
    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    name : str
        Name of the author.
    title : str
        Title of the author, typically a position.
    summary : str
        Summary text displayed below the author.

    Returns
    -------
    None
    """
    template = env.get_template("author-summary.html")
    body = template.render(src=src, name=name, title=title, summary=summary)
    st.html(body)


def content_card(
    src: str, caption: str, href: str, tag: str = "news", width: int = 12
) -> None:
    """
    [Content card](https://design.undp.org/?path=/docs/components-ui-components-cards-content-card-with-image--docs) component
    (with image).

    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    caption : str
        Caption text displayed below the image.
    href : str
        URL the component points to when clicked.
    tag : str, default="news"
        Tag text shown above the image.
    width : int, default=12
        Component width using a 12-grid scheme.

    Returns
    -------
    None
    """
    kwargs = locals()
    template = env.get_template("content-card.html")
    body = template.render(**kwargs)
    st.html(body)


def download_card(
    src: str | None,
    title: str,
    format: str,
    href: str,
    variant: Literal["publication", "card", "default"] = "default",
) -> None:
    """
    [Download card](https://design.undp.org/?path=/docs/components-ui-components-cards-download-card--docs) component.

    Parameters
    ----------
    src : str | None
        Image `src` attribute that can be a local path or URL to an image.
    title : str
        Title of the document displayed on the card.
    format : str
        Format of the file displayed on the card, including file size, e.g., "PDF (800kb)".
    href : str
        URL the component points to when clicked, typically a download link.
    variant : Literal["publication", "card", "default"], default="default"
        One of the three card variants. If "default", `src` should be set to `None`.

    Returns
    -------
    None
    """
    if variant != "default":
        template = env.get_template("download-card-image.html")
        image = template.render(src=src, variant=variant)
    else:
        image = ""
    template = env.get_template("download-card.html")
    body = template.render(title=title, format=format, image=image, href=href)
    st.html(body)


def featured_card(
    src: str,
    title: str,
    summary: str,
    href: str,
    tag: str = "news",
    width: int = 12,
) -> None:
    """
    [Featured card](https://design.undp.org/?path=/docs/components-ui-components-cards-featured-card--docs) component.

    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    title : str
        Title displayed on the card in bold.
    summary : str
        Summary text displayed below the title.
    href : str
        URL the component points to when clicked.
    tag : str, default="news"
        Tag text shown above the title.
    width : int, default=12
        Component width using a 12-grid scheme.

    Returns
    -------
    None
    """
    kwargs = locals()
    template = env.get_template("featured-card.html")
    body = template.render(**kwargs)
    st.html(body)


def image_card(src: str, summary: str, href: str, width: int = 12) -> None:
    """
    [Image reveal card](https://design.undp.org/?path=/docs/components-ui-components-cards-image-reveal-card--docs) component.

    Parameters
    ----------
    src : str
        Image `src` attribute that can be a local path or URL to an image.
    summary : str
        Summary text displayed below the image.
    href : str
        URL the component points to when clicked.
    width : int, default=12
        Component width using a 12-grid scheme.

    Returns
    -------
    None
    """
    kwargs = locals()
    template = env.get_template("image-card.html")
    body = template.render(**kwargs)
    st.html(body)


def breadcrumb(items: list[dict[str, str]]) -> None:
    """
    [Breadcrumbs](https://design.undp.org/?path=/docs/components-navigation-components-breadcrumbs--docs) component.

    Parameters
    ----------
    items : list[dict[str, str]
        List of items where each item maps a title to a URL.

    Returns
    -------
    None
    """
    template = env.get_template("breadcrumb.html")
    body = template.render(items=items)
    st.html(body)


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
    None
    """
    body = f"""
        <div class='stat-card-smaller'>
            <h3>{value}</h3>
            <h4>{title}</h4>
            <p>{text}</p>
        </div>
    """
    st.html(body)
