import plotly.graph_objects as go
import streamlit as st

import st_undp

tabs = st.tabs(
    [
        "DIY",
        "Area Chart",
        "Beeswarm Chart",
        "Butterfly Chart",
        "Circle Packing Chart",
        "Donut Chart",
        "Dual Axes Chart",
        "Dumbbell Chart",
        "Grouped Bar Chart",
        "Heatmap",
        "Histogram",
        "Line Chart",
        "Multi-line Chart",
        "Pie Chart",
        "Scatter Plot",
        "Simple Bar Chart",
        "Sparkline Chart",
        "Stacked Bar Chart",
    ]
)

with tabs[0]:
    data = {"categories": ["A", "B", "C"], "values": [10, 20, 30]}

    fig = go.Figure(
        data=[go.Bar(y=data["categories"], x=data["values"], orientation="h")]
    )
    fig.update_layout(title="DIY Custom Plot", xaxis_title="values", yaxis_title="categories")

    fig.add_annotation(
        text="Source: Example Data",
        xref="paper",
        yref="paper",
        x=0,
        y=-0.2,
        showarrow=False,
    )

    fig.add_shape(
        type="line",
        x0=20,
        x1=20,
        y0=0,
        y1=len(data["categories"]),
        line=dict(color="black", width=1, dash="dash"),
    )
    st.plotly_chart(fig)

    with st.expander("Show Code"):
        st.code(
            """
            data = {"categories": ["A", "B", "C"], "values": [10, 20, 30]}

            fig = go.Figure(
            data=[go.Bar(y=data["categories"], x=data["values"], orientation='h')]
        )
        fig.update_layout(title="DIY Custom Plot", xaxis_title="values", yaxis_title="categories")


        fig.add_annotation(
            text="Source: Example Data",
            xref="paper",
            yref="paper",
            x=0,
            y=-0.2,
            showarrow=False,
        )

        fig.add_shape(
            type="line",
            x0=20,
            x1=20,
            y0=0,
            y1=len(data["categories"]),
            line=dict(color="black", width=1, dash="dash"),
        )
        st.plotly_chart(fig)
            """
        )

with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Area Chart", key="area_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="area_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="area_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)", "Source: Example Data", key="area_annotation"
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="area_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="area_y",
        )

    with col2:
        area_data = {"x": [1, 2, 3, 4, 5], "y": [5, 10, 15, 20, 25]}

        st_undp.area_chart(
            area_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.area_chart(area_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[2]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Beeswarm Chart", key="beeswarm_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="beeswarm_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="beeswarm_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="beeswarm_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="beeswarm_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="beeswarm_y",
        )

    with col2:
        beeswarm_data = {"x": [1, 2, 3, 4, 5], "y": [10, 14, 12, 18, 22]}

        st_undp.beeswarm_chart(
            beeswarm_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.beeswarm_chart(beeswarm_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[3]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Butterfly Chart", key="butterfly_title")
        x_title = st.text_input("X Axis Title", "Values", key="butterfly_x_title")
        y_title = st.text_input("Y Axis Title", "Categories", key="butterfly_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="butterfly_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="butterfly_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="butterfly_y",
        )

    with col2:
        butterfly_data = {
            "categories": ["A", "B", "C"],
            "values1": [10, 20, 30],
            "values2": [15, 25, 35],
        }

        st_undp.butterfly_chart(
            butterfly_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.butterfly_chart(butterfly_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[4]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input(
            "Chart Title", "Circle Packing Chart", key="circle_packing_title"
        )
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="circle_packing_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="circle_packing_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="circle_packing_y",
        )

    with col2:
        circle_packing_data = {
            "x": [1, 2, 3, 4, 5],
            "y": [10, 14, 12, 18, 22],
            "sizes": [10, 20, 30, 40, 50],
        }

        st_undp.circle_packing_chart(
            circle_packing_data,
            title=title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.circle_packing_chart(circle_packing_data, title='{title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[5]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Donut Chart", key="donut_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)", "Source: Example Data", key="donut_annotation"
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="donut_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="donut_y",
        )

    with col2:
        donut_data = {
            "labels": ["Category A", "Category B", "Category C", "Category D"],
            "values": [4500, 2500, 1050, 2002],
        }

        st_undp.donut_chart(
            donut_data,
            title=title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.donut_chart(donut_data, title='{title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[6]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Dual Axes Chart", key="dual_axes_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="dual_axes_x_title")
        y_title1 = st.text_input("Y Axis Title 1", "Y Axis 1", key="dual_axes_y_title1")
        y_title2 = st.text_input("Y Axis Title 2", "Y Axis 2", key="dual_axes_y_title2")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="dual_axes_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="dual_axes_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="dual_axes_y",
        )

    with col2:
        dual_axes_data = {
            "x": [1, 2, 3, 4, 5],
            "y1": [6, 18, 13, 17, 20],
            "y2": [19, 12, 23, 27, 30],
        }

        st_undp.dual_axes_chart(
            dual_axes_data,
            title=title,
            x_title=x_title,
            y_title1=y_title1,
            y_title2=y_title2,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.dual_axes_chart(dual_axes_data, title='{title}', x_title='{x_title}', y_title1='{y_title1}', y_title2='{y_title2}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[7]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Dumbbell Chart", key="dumbbell_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="dumbbell_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="dumbbell_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="dumbbell_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="dumbbell_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="dumbbell_y",
        )

    with col2:
        dumbbell_data = {
            "x1": [1, 2, 3, 4, 5],
            "x2": [2, 3, 4, 5, 6],
            "y": [10, 14, 12, 18, 22],
        }

        st_undp.dumbbell_chart(
            dumbbell_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.dumbbell_chart(dumbbell_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[8]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input(
            "Chart Title", "Grouped Bar Chart", key="grouped_bar_title"
        )
        x_title = st.text_input("X Axis Title", "Categories", key="grouped_bar_x_title")
        y_title = st.text_input("Y Axis Title", "Values", key="grouped_bar_y_title")
        orient = st.selectbox(
            "Orientation (Vertical/Horizontal)",
            ["v", "h"],
            0,
            key="grouped_bar_orientation",
        )
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="grouped_bar_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="grouped_bar_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="grouped_bar_y",
        )

    with col2:
        grouped_bar_data = {
            "categories": ["A", "B", "C"],
            "groups": [
                {"name": "Group 1", "values": [10, 20, 30]},
                {"name": "Group 2", "values": [15, 25, 35]},
            ],
        }

        st_undp.grouped_bar_chart(
            grouped_bar_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            orient=orient,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.grouped_bar_chart(grouped_bar_data, title='{title}', x_title='{x_title}', y_title='{y_title}', orient='{orient}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[9]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Heatmap", key="heatmap_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="heatmap_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="heatmap_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="heatmap_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="heatmap_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="heatmap_y",
        )
        color_scale_options = {
        "Neutral Colors": st_undp.undp_colors["sequentialColors"]["neutralColorsx10"],
        "Positive Colors": st_undp.undp_colors["sequentialColors"]["positiveColorsx10"],
        "Negative Colors": st_undp.undp_colors["sequentialColors"]["negativeColorsx10"],
        "Diverging Colors": st_undp.undp_colors["divergentColors"]["colorsx10"]
        }
        selected_color_scale = st.selectbox("Select Color Scale", list(color_scale_options.keys()), 0, key="select-heatmap-colorscale")


    with col2:
        heatmap_data = {
            "z": [[1, 4, 7], [8, 4, 7], [10, 6, 9]],
            "x": ["A", "B", "C"],
            "y": ["X", "Y", "Z"],
        }

        st_undp.heatmap(
            heatmap_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
            colorscale=color_scale_options[selected_color_scale]
        )
        code = f"""
st_undp.heatmap(heatmap_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y}, colorscale={color_scale_options[selected_color_scale]})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[10]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Histogram", key="hist_title")
        x_title = st.text_input("X Axis Title", "Values", key="hist_x_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)", "Source: Example Data", key="hist_annotation"
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="hist_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="hist_y",
        )

    with col2:
        histogram_data = {"values": [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]}

        st_undp.histogram(
            histogram_data,
            title=title,
            x_title=x_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.histogram(histogram_data, title='{title}', x_title='{x_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[11]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Line Chart", key="line_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="line_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="line_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)", "Source: Example Data", key="line_annotation"
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="line_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="line_y",
        )

    with col2:
        line_data = {"x": [1, 2, 3, 4, 5], "y": [10, 15, 13, 17, 20]}

        st_undp.line_chart(
            line_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.line_chart(line_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[12]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Multi-line Chart", key="multiline_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="multiline_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="multiline_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="multiline_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="multiline_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="multiline_y",
        )

    with col2:
        multiline_data = {
            "lines": [
                {"name": "Line 1", "x": [1, 2, 3, 4, 5], "y": [10, 15, 13, 17, 20]},
                {"name": "Line 2", "x": [1, 2, 3, 4, 5], "y": [20, 25, 23, 27, 30]},
            ]
        }

        st_undp.multiline_chart(
            multiline_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.multiline_chart(multiline_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[13]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Pie Chart", key="pie_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)", "Source: Example Data", key="pie_annotation"
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="pie_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="pie_y",
        )

    with col2:
        pie_data = {
            "labels": ["Category A", "Category B", "Category C"],
            "values": [4500, 2500, 1050],
        }

        st_undp.pie_chart(
            pie_data,
            title=title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.pie_chart(pie_data, title='{title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)


with tabs[14]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Scatter Plot", key="scatter_title")
        x_title = st.text_input("X Axis Title", "X Axis", key="scatter_x_title")
        y_title = st.text_input("Y Axis Title", "Y Axis", key="scatter_y_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="scatter_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="scatter_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="scatter_y",
        )

    with col2:
        scatter_data = {"x": [1, 2, 3, 4, 5], "y": [10, 14, 12, 18, 22]}

        st_undp.scatter_plot(
            scatter_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.scatter_plot(scatter_data, title='{title}', x_title='{x_title}', y_title='{y_title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[15]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Simple Bar Chart")
        x_title = st.text_input("X Axis Title", "Values")
        y_title = st.text_input("Y Axis Title", "Categories")
        orient = st.selectbox(
            "Orientation (Vertical/Horizontal)",
            ["v", "h"],
            1,
            key="simple_bar_orientation",
        )
        annotation = st.text_input("Annotation (e.g., Source)", "Source: Example Data")
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)", min_value=0.0, max_value=1.0, value=0.0
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)", min_value=-1.0, max_value=1.0, value=-0.3
        )
        reference_line = st.number_input("Reference Line", value=None)

    with col2:
        bar_data = {"categories": ["A", "B", "C"], "values": [10, 20, 30]}

        st_undp.simple_bar_chart(
            bar_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            orient=orient,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
            reference_line=reference_line,
        )
        code = f"""
st_undp.horizontal_bar_chart(bar_data, title='{title}', x_title='{x_title}', y_title='{y_title}', orient='{orient}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[16]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("Chart Title", "Sparkline Chart", key="sparkline_title")
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="sparkline_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="sparkline_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="sparkline_y",
        )

    with col2:
        sparkline_data = {"x": [1, 2, 3, 4, 5], "y": [10, 15, 13, 17, 20]}

        st_undp.sparkline_chart(
            sparkline_data,
            title=title,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.sparkline_chart(sparkline_data, title='{title}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)

with tabs[17]:
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input(
            "Chart Title", "Stacked Bar Chart", key="stacked_bar_title"
        )
        x_title = st.text_input("X Axis Title", "Categories", key="stacked_bar_x_title")
        y_title = st.text_input("Y Axis Title", "Values", key="stacked_bar_y_title")
        orient = st.selectbox(
            "Orientation (Vertical/Horizontal)",
            ["v", "h"],
            0,
            key="stacked_bar_orientation",
        )
        annotation = st.text_input(
            "Annotation (e.g., Source)",
            "Source: Example Data",
            key="stacked_bar_annotation",
        )
        annotation_x = st.number_input(
            "Annotation X Position (0 to 1)",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            key="stacked_bar_x",
        )
        annotation_y = st.number_input(
            "Annotation Y Position (0 to 1)",
            min_value=-1.0,
            max_value=1.0,
            value=-0.3,
            key="stacked_bar_y",
        )

    with col2:
        stacked_bar_data = {
            "categories": ["A", "B", "C"],
            "groups": [
                {"name": "Group 1", "values": [10, 20, 30]},
                {"name": "Group 2", "values": [15, 25, 35]},
            ],
        }

        st_undp.stacked_bar_chart(
            stacked_bar_data,
            title=title,
            x_title=x_title,
            y_title=y_title,
            orient=orient,
            annotation=annotation,
            annotation_x=annotation_x,
            annotation_y=annotation_y,
        )
        code = f"""
st_undp.stacked_bar_chart(stacked_bar_data, title='{title}', x_title='{x_title}', y_title='{y_title}', orient='{orient}', annotation='{annotation}', annotation_x={annotation_x}, annotation_y={annotation_y})
        """
        with st.expander("Show Code"):
            st.code(code)
