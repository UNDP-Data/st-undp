"""
A simple Streamlit application testing and showcasing the package.
"""

import streamlit as st

import st_undp

OPTIONS = list("ABCDE")

st.set_page_config(
    page_title="st-undp App",
    page_icon=":flag-un:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/undp-data/st-undp",
        "Report a Bug": "https://github.com/undp-data/st-undp/issues",
        "About": None,
    },
)

st_undp.apply_style()

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Regular text.")

st.markdown("More regular text with an [example link](https://data.undp.org).")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Buttons", "Forms", "Alerts", "Custom Components", "Footer"]
)

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        if clicked := st.button("Button (primary)", type="primary"):
            st.write(f"Clicked: {clicked}")
    with col2:
        if clicked := st.button("Button (secondary)", type="secondary"):
            st.write(f"Clicked: {clicked}")
with tab2:
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

with tab3:
    st.success("Success", icon=":material/check_circle:")
    st.info("Info", icon=":material/info:")
    st.warning("Warning", icon=":material/warning:")
    st.error("Error", icon=":material/error:")

with tab4:
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

with tab5:
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
