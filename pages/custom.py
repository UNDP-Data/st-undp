import streamlit as st

import st_undp

OPTIONS = list("ABCDE")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(
    [
        "Author",
        "Author Card",
        "Author Summary",
        "Breadcrumb",
        "Content Card",
        "Download Card",
        "Featured Card",
        "Footer",
        "Header",
        "Image Card",
        "Stats Card",
    ]
)
with tab1:
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

with tab2:
    code = """
    st_undp.author_card(
        src="app/static/aristotle.jpg",
        name="Aristotle",
        title="Ancient Greek philosopher and polymath",
        summary="His writings cover a broad range of subjects spanning the natural sciences, philosophy, linguistics, economics, politics, psychology, and the arts.",
        href="https://en.wikipedia.org/wiki/Aristotle",
    )
    """
    eval(code.strip())
    with st.expander("Show Code"):
        st.code(code)

with tab3:
    code = """
    st_undp.author_summary(
        src="app/static/aristotle.jpg",
        name="Aristotle",
        title="Ancient Greek philosopher and polymath",
        summary="As the founder of the Peripatetic school of philosophy in the Lyceum in Athens, he began the wider Aristotelian tradition that followed, which set the groundwork for the development of modern science."
    )
    """
    eval(code.strip())
    with st.expander("Show Code"):
        st.code(code)

with tab4:
    code = """
        st_undp.breadcrumb([
            {'label': 'Home', 'url': '/'},
            {'label': 'Custom components', 'url': '/custom'},
            {'label': 'Breadcrumb', 'url': None}
        ])
        """
    eval(code.strip())
    with st.expander("Show Code"):
        st.code(code)

with tab5:
    st.subheader("Content Card")
    body = "Use st.columns to arrange multiple cards in a row."
    st.info(body, icon=":material/lightbulb:")
    code = """
    st_undp.content_card(
        src="app/static/aristotle.jpg",
        caption="Nicomachean Ethics is closely related to Eudemian Ethics",
        href="https://en.wikipedia.org/wiki/Nicomachean_Ethics",
        tag="announcement",
    )
    """.strip()
    col1, col2 = st.columns(2)
    rows = col1.slider("Rows", min_value=1, max_value=5, value=2)
    cols = col2.slider("Columns", min_value=2, max_value=5, value=4)
    for _ in range(rows):
        for col in st.columns(cols):
            with col:
                eval(code)
    with st.expander("Show Code"):
        st.code(code)

with tab6:
    code = """
    st_undp.download_card(
        src="app/static/aristotle.jpg",
        title="Corpus Aristotelicum",
        format="PDF (1.5MB)",
        href="https://en.wikipedia.org/wiki/Works_of_Aristotle",
        variant="{}",
    )
    """.strip()
    for col, variant in zip(st.columns(3), ("publication", "card", "default")):
        with col:
            eval(code.format(variant))
            with st.expander("Show Code"):
                st.code(code.format(variant))

with tab7:
    code = """
    st_undp.featured_card(
       src="app/static/aristotle.jpg",
       title="Nicomachean Ethics",
       summary="Aristotle's best-known works on ethics: the science of the good for human life, that which is the goal or end at which all our actions aim",
       href="https://en.wikipedia.org/wiki/Nicomachean_Ethics",
       width=6,
    )
    """.strip()
    eval(code)
    with st.expander("Show Code"):
        st.code(code)

with tab8:
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

with tab9:
    logo = st.radio("Logo", ("UNDP", "PNUD"), key="logo", horizontal=True)
    title = st.text_input("Header Title", key="title")
    subtitle = st.text_input("Header Subtitle", key="subtitle")
    code = f"""
    st_undp.header(
        title="{title}",
        subtitle="{subtitle}",
        logo="{logo.lower()}",
    )
    """.strip()
    with st.expander("Show Code"):
        st.code(code)

with tab10:
    code = """
    st_undp.image_card(
       src="app/static/aristotle.jpg",
       summary="Nicomachean Ethics is Aristotle's best-known works on ethics: the science of the good for human life, that which is the goal or end at which all our actions aim",
       href="https://en.wikipedia.org/wiki/Nicomachean_Ethics",
       width=3,
    )
    """.strip()
    eval(code)
    with st.expander("Show Code"):
        st.code(code)

with tab11:
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
