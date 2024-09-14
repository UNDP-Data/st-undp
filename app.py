"""
A simple Streamlit application testing and showcasing the package.
"""

import streamlit as st

import st_undp

OPTIONS = list("ABCDE")

st_undp.set_page_config(
    title="st-undp App",
    menu_items={
        "Get help": "https://github.com/undp-data/st-undp",
        "Report a Bug": "https://github.com/undp-data/st-undp/issues",
        "About": "Developed with [st-undp](https://github.com/undp-data/st-undp).",
    },
)

st_undp.apply_style()

st.title("Title")
st.header("Header")
st.subheader("Subheader")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    [
        "Alerts",
        "Buttons",
        "Custom Components",
        "Footer",
        "Forms",
        "Logo",
        "Sidebar",
        "Text",
    ]
)

with tab1:
    st.success("Success", icon=":material/check_circle:")
    st.info("Info", icon=":material/info:")
    st.warning("Warning", icon=":material/warning:")
    st.error("Error", icon=":material/error:")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        if clicked := st.button("Button (primary)", type="primary"):
            st.write(f"Clicked: {clicked}")
    with col2:
        if clicked := st.button("Button (secondary)", type="secondary"):
            st.write(f"Clicked: {clicked}")

with tab3:
    st.subheader("Author")
    code = """
    st_undp.author(
        src="app/static/aristotle.jpg",
        name="Aristotle",
        title="Ancient Greek philosopher and polymath",
        href="https://en.wikipedia.org/wiki/Aristotle",
    )
    """
    eval(code.strip())
    with st.expander("Show Code"):
        st.code(code)

    st.subheader("Stats Cards")
    col1, col2 = st.columns(2)
    with col1:
        code = """
            st_undp.stats_card(
                value=3.14,
                title="Pi",
                text="Pi is a mathematical constant that is the ratio of a circle's circumference to its diameter",
            )
            """
        eval(code.strip())
        with st.expander("Show Code"):
            st.code(code)
    with col2:
        code = """
            st_undp.stats_card(
                value=2.71,
                title="Euler's constant",
                text="Euler's constant is  is a mathematical constant, defined as the limiting difference between the harmonic series and the natural logarithm",
            )
            """
        eval(code.strip())
        with st.expander("Show Code"):
            st.code(code)

with tab4:
    body = "Make sure to call the footer function at the bottom of your script outside of any tab, column etc."
    st.info(body, icon=":material/lightbulb:")
    footer = st.radio(
        label="Footer",
        options=("None", "UNDP (Default)", "UNDP DFx", "Custom"),
        index=0,
    )

    footer = footer.lower()
    if "default" in footer:
        code = """st_undp.footer()"""
    elif "dfx" in footer:
        code = """st_undp.footer("dfx")"""
    elif "custom" in footer:
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
        st.json(columns)
        code = """st_undp.footer(columns)"""
    else:
        code = "None"
    with st.expander("Show Code"):
        st.code(code)
    eval(code)

with tab5:
    with st.form("form"):
        st.radio("Radio", OPTIONS, horizontal=True)
        st.number_input("Number input")
        col1, col2 = st.columns(2)
        with col1:
            st.checkbox("Checkbox")
            st.selectbox("Selectbox", OPTIONS)
            st.select_slider("Slider", OPTIONS)
            st.date_input("Date input")
            st.text_input("Text input (default)", type="default")
        with col2:
            st.toggle("Toggle")
            st.multiselect("Multiselect", OPTIONS)
            st.slider("Slider")
            st.time_input("Time input")
            st.text_input("Text input (password)", type="password")
        st.text_area("Text area")
        st.color_picker("Colour picker")
        st.file_uploader("File uploader")

        submitted = st.form_submit_button("Form submit button", type="primary")
        if submitted:
            st.json(st.session_state)

with tab6:
    title = st.text_input("Header Title", value="Data Futures \A Exchange")
    name = st.radio("Name", ("UNDP", "PNUD"), horizontal=True)
    colour = st.radio("Colour", ("Blue", "White"), horizontal=True)
    if colour.lower() == "white":
        message = """The white logo is not visible in the light theme. 
        Change the theme to dark to verify it is there. 
        However, the dark theme is discouraged in production as the styling is specifically designed for the light theme."""
        st.info(message, icon=":material/lightbulb:")
    code = f"""st_undp.logo(name="{name.lower()}", title="{title}", colour="{colour.lower()}")"""
    with st.expander("Show Code"):
        st.code(code)
    eval(code)

with tab7:
    if st.toggle("Sidebar"):
        with st.sidebar:
            st.subheader("Sidebar Title")
            with st.container():
                st.info("There could be your content.", icon=":material/lightbulb:")

with tab8:
    st.markdown("Regular text with an [example link](https://data.undp.org).")
    st.text("Do not use `st.text`. Its content will not be properly styled.")
