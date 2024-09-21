# Usage

The package can be used to style your existing Streamlit app with just a couple of lines of code. Alternatively, you
can use custom components provided by the package to build more advanced applications in line with UNDP Design System.

## Basic Usage

The package is intended to make styling a breeze. The most basic usage involves only two simple steps.

First, use the CLI to set up the recommended theme in `.streamlit/config.toml`:

```shell
python -m st_undp configure
```

This will edit the theme section in the file if it exists or create it if it doesn't.
Then, call `apply_style` function inside your application entry point, typically `app.py`: 

```python hl_lines="4"
import st_undp
import streamlit as st

st_undp.apply_style()  # call this before any other streamlit function

st.title("Hello world!")  # now UNDP-styled
```

Once you apply the style, most streamlit components will be properly styled and work out-of-the box. Note that
[`st_undp.apply_style`](reference.md/#st_undp.apply_style) calls `st.set_page_config` internally
and sets the required settings, including the favicon.

## Recommended Usage

In addition to styles, the package provides custom components to help you build even 
better-looking UNDP-styled apps. Two of these components are strongly recommended for all applications.
These are the header and the footer.

### Header

Use [`st_undp.header`](reference.md/#st_undp.header) to add the 
[header component](https://design.undp.org/?path=/story/components-navigation-components-main-navigation-country-header--country-header)
that includes the official logo.

```python hl_lines="6-10"
import st_undp
import streamlit as st

st_undp.apply_style()

st_undp.header(
    title="Data Futures Exchange",
    subtitle="st-undp Application",
    logo="undp",  # set to "pnud" for French/Spanish
)

st.title("Hello world!")
```

If you are building a [multipage application](https://docs.streamlit.io/develop/concepts/multipage-apps),
use the header component to create navigation. Assuming you defined your pages in `pages/` directory,
use a list of pages to add navigation.

```python hl_lines="6-18 23 29-31"
import st_undp
import streamlit as st

st_undp.apply_style()

# define the pages
pages = [
    st.Page(
        page="pages/page1.py",
        title="first page",
        url_path="./",  # use this pattern and not the `default` parameter
    ),
    st.Page(
        page="pages/page2.py",
        title="second page",
        url_path="/second",
    ),
]

st_undp.header(
    title="Data Futures Exchange",
    subtitle="st-undp Application",
    pages=pages,  # pass a list of `st.Page` items to add navigation
    logo="undp",
)

st.title("Hello world!")

# run the pages
pg = st.navigation(pages=pages, position="hidden")  # set position to "hidden"
pg.run()
```

### Footer

Add a UNDP-styled footer with [`st_undp.footer`](reference.md/#st_undp.footer). You can choose between the default UNDP footer,
the footer used by the Data Futures Exchange or create your custom one.

```python hl_lines="8"
import st_undp
import streamlit as st

st_undp.apply_style()

st.title("Hello world!")

st_undp.footer("dfx")  # call it at the end of your script
```

To create a custom footer, pass a dictionary whose values are dictionaries too. The keys of the
outer dictionary will be used as column names while the keys and values of the inner dictionaries will
be interpreted as column items and their links respectively. Here is an example:

```python hl_lines="8-21"
import st_undp
import streamlit as st

st_undp.apply_style()

st.title("Hello world!")

# custom footer items
columns = {
    "focus areas": {
        "Energy": "https://data.undp.org/energy",
        "Environment": "https://data.undp.org/environment",
        "Governance": "https://data.undp.org/governance",
    },
    "about us": {
        "About DFx": "https://data.undp.org/about",
        "Our Partners": "https://data.undp.org/our-partners",
        "Contact Us": "https://data.undp.org/contact-us",
    },
}
st_undp.footer(columns)
```

## Advanced Usage

For even more demanding use cases, you can use additional custom components to create breadcrumbs,
summaries and various types of cards.

### Stats Card

Use [`st_undp.stats_card`](reference.md/#st_undp.stats_card) to create a [stats card](https://design.undp.org/iframe?viewMode=story&id=components-ui-components-cards-stats-card--stats-card&args=) component.

```python hl_lines="8-12 14-18"
import st_undp
import streamlit as st

st_undp.apply_style()

st.title("Hello world!")

st_undp.stats_card(
    value=3.14,
    title="Pi",
    text="The ratio of a circle's circumference to its diameter",
)
```

If you have multiple cards, you can easily arrange them in one row with `st.columns`.

```python hl_lines="8 10 17"
import st_undp
import streamlit as st

st_undp.apply_style()

st.title("Hello world!")

col1, col2 = st.columns(2)

with col1:
    st_undp.stats_card(
        value=3.14,
        title="Pi",
        text="The ratio of a circle's circumference to its diameter",
    )

with col2:
    st_undp.stats_card(
        value=2.71,
        title="Euler's constant",
        text="The limiting difference between the harmonic series and the natural logarithm",
    )
```
