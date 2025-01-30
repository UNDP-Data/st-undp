import streamlit as st

OPTIONS = list("ABCDE")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Alerts",
        "Buttons",
        "Forms",
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

with tab4:
    if st.toggle("Sidebar"):
        with st.sidebar:
            st.subheader("Sidebar Title")
            with st.container():
                st.info("There could be your content.", icon=":material/lightbulb:")
                search = st.text_input("Search")
                tags = st.multiselect("Tags", OPTIONS)
                clicked = st.button("Search", type="primary")
        if clicked:
            st.subheader("Search Parameters")
            st.json({"search": search, "tags": tags})


with tab5:
    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.markdown("Regular text with an [example link](https://data.undp.org).")
    st.text("Do not use `st.text`. Its content will not be properly styled.")
    st.markdown("Code sections looks as follows `print(f'hello streamlit app')` ")
    for item in [
        {
            "header": "An expander",
            "body": "This is an expander with an [example link](https://data.undp.org)",
        }
    ]:
        with st.expander(item["header"]):
            st.write(item["body"])
