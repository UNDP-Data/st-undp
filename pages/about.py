import streamlit as st

import st_undp

st.info(
    """
This application has been developed with [st-undp](https://github.com/undp-data/st-undp) package, open-sourced as part of 
AI as a Service offering from the Data Futures Exchange (DFx) at UNDP.
"""
)

col1, col2, col3 = st.columns(3)
with col1:
    st_undp.featured_card(
        src="app/static/dfx.jpg",
        title="Data Futures Exchange",
        summary="Explore the central hub for data innovation for development impact, guided by UNDP’s thematic focus areas",
        href="https://data.undp.org",
        tag="resource",
    )
with col2:
    st_undp.featured_card(
        src="app/static/aiaas.jpg",
        title="AI as a Service",
        summary="Embrace data science tools and services to help you gain insights into the impact of development policies",
        href="https://data.undp.org/what-we-do/ai-as-service",
        tag="resource",
    )
with col3:
    st_undp.featured_card(
        src="app/static/github.jpg",
        title="UNDP Data GitHub",
        summary="Leverage open source projects for data visualisation, geospatial analytics and artificial intelligence",
        href="https://github.com/undp-data",
        tag="resource",
    )
