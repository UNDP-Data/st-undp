"""
    extras component 
        eg. Plotly charts
"""

import streamlit as st


def insert_controls(prefix: str) -> dict:
    """
    Takes in a string that serves as a prefix for the keys of the input controls, and
    creates a set of input controls for Plotly chart customization.

    Returns:
        A dictionary containing the following keys and their corresponding user input values:
    """
    controls_dict = {
        "title": st.text_input(
            "Chart Title", f"{prefix.capitalize()} chart", key=f"{prefix}_title"
        ),
        "x_title": st.text_input("X Axis Title", "X Axis", key=f"{prefix}_x_title"),
        "y_title": st.text_input("Y Axis Title", "Y Axis", key=f"{prefix}_y_title"),
        "annotation": st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key=f"{prefix}_annotation",
        ),
        "annotation_x": st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key=f"{prefix}_annotation_x",
        ),
        "annotation_y": st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key=f"{prefix}_annotation_y",
        ),
    }
    return controls_dict


tabs = st.tabs(
    [
        "Area Chart",
        "Butterfly Chart",
        "Donut Chart",
        "Grouped Bar Chart",
        "Heatmap",
        "Simple Bar Chart",
        "Stacked Bar Chart",
    ]
)

with tabs[0]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("area")
    with col2:
        area_data = {"x": [1, 2, 3, 4, 5], "y": [5, 10, 15, 20, 25]}
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(x={area_data['x']}, y={area_data['y']}, fill='tozeroy'))
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("butterfly")
    with col2:
        butterfly_data = {
            "categories": ["A", "B", "C"],
            "values1": [10, 20, 30],
            "values2": [15, 25, 35],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Bar(x={butterfly_data['values1']}, y={butterfly_data['categories']}, name='Group 1', orientation='h'))
fig.add_trace(go.Bar(x=[-v for v in {butterfly_data['values2']}], y={butterfly_data['categories']}, name='Group 2', orientation='h'))
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}', barmode='overlay')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[2]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("donut")
    with col2:
        donut_data = {
            "labels": ["Category A", "Category B", "Category C", "Category D"],
            "values": [4500, 2500, 1050, 2002],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure(data=[go.Pie(labels={donut_data['labels']}, values={donut_data['values']}, hole=0.4)])
fig.update_layout(title='{controls['title']}')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[3]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("grouped_bar")
    with col2:
        grouped_bar_data = {
            "categories": ["Category 1", "Category 2", "Category 3"],
            "groups": [
                {"name": "Group 1", "values": [10, 20, 30]},
                {"name": "Group 2", "values": [15, 25, 35]},
            ],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure()
for group in {grouped_bar_data['groups']}:
    fig.add_trace(go.Bar(x={grouped_bar_data['categories']}, y=group['values'], name=group['name']))
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}', barmode='group')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[4]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("heatmap")
    with col2:
        heatmap_data = {
            "z": [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
            "x": ["X1", "X2", "X3"],
            "y": ["Y1", "Y2", "Y3"],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure(data=go.Heatmap(z={heatmap_data['z']}, x={heatmap_data['x']}, y={heatmap_data['y']}, colorscale=['#FFF4AC', '#C8E7A8', '#8CD8A4', '#47C79F', '#00B29C', '#0099A5', '#007FAF', '#0067AD', '#005396', '#003F80'], colorbar=dict(
    orientation='h',
    x=0.5,
    y=1.1,
    xanchor='center',
    yanchor='bottom',
    title='scale'
)))
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[5]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("simple bar")
    with col2:
        simple_bar_data = {
            "categories": ["Category A", "Category B", "Category C"],
            "values": [10, 20, 30],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure(data=[go.Bar(y={simple_bar_data['categories']}, x={simple_bar_data['values']})])
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)

with tabs[6]:
    col1, col2 = st.columns(2)
    with col1:
        controls = insert_controls("stacked bar")
    with col2:
        stacked_bar_data = {
            "categories": ["Category 1", "Category 2", "Category 3"],
            "groups": [
                {"name": "Group 1", "values": [10, 20, 30]},
                {"name": "Group 2", "values": [15, 25, 35]},
            ],
        }
        code_body = f"""
import plotly.graph_objects as go
fig = go.Figure()
for group in {stacked_bar_data['groups']}:
    fig.add_trace(go.Bar(x={stacked_bar_data['categories']}, y=group['values'], name=group['name']))
fig.update_layout(title='{controls['title']}', xaxis_title='{controls['x_title']}', yaxis_title='{controls['y_title']}', barmode='stack')
if '{controls['annotation']}' != '':
    fig.add_annotation(text='{controls['annotation']}', xref='paper', yref='paper', x={controls['annotation_x']}, y={controls['annotation_y']}, showarrow=False)
st.plotly_chart(fig)"""
        exec(code_body.strip())
        with st.expander("Show Code"):
            st.code(code_body)
