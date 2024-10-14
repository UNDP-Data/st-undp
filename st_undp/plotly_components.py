import streamlit as st
import plotly.graph_objects as go

def area_chart(
    data,
    title="Area Chart",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(data=[go.Scatter(x=data["x"], y=data["y"], fill="tozeroy")])
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def beeswarm_chart(
    data,
    title="Beeswarm Chart",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(
        data=[
            go.Scatter(x=data["x"], y=data["y"], mode="markers", marker=dict(size=12))
        ]
    )
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def butterfly_chart(
    data,
    title="Butterfly Chart",
    x_title="Values",
    y_title="Categories",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(y=data["categories"], x=data["values1"], name="Group 1", orientation="h")
    )
    fig.add_trace(
        go.Bar(
            y=data["categories"],
            x=[-val for val in data["values2"]],
            name="Group 2",
            orientation="h",
        )
    )
    fig.update_layout(
        title=title, xaxis_title=x_title, yaxis_title=y_title, barmode="relative"
    )
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def circle_packing_chart(
    data,
    title="Circle Packing Chart",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(
        data=[
            go.Scatter(
                x=data["x"],
                y=data["y"],
                mode="markers",
                marker=dict(size=data["sizes"]),
            )
        ]
    )
    fig.update_layout(title=title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def donut_chart(
    data, title="Donut Chart", annotation=None, annotation_x=0.5, annotation_y=-0.2
):
    fig = go.Figure(
        data=[go.Pie(labels=data["labels"], values=data["values"], hole=0.3)]
    )
    fig.update_layout(title=title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def dumbbell_chart(
    data,
    title="Dumbbell Chart",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["x1"], y=data["y"], mode="markers", name="Start"))
    fig.add_trace(go.Scatter(x=data["x2"], y=data["y"], mode="markers", name="End"))
    for i in range(len(data["y"])):
        fig.add_shape(
            type="line",
            x0=data["x1"][i],
            y0=data["y"][i],
            x1=data["x2"][i],
            y1=data["y"][i],
            line=dict(color="gray", width=2),
        )
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def dual_axes_chart(
    data,
    title="Dual Axes Chart",
    x_title="X Axis",
    y_title1="Y Axis 1",
    y_title2="Y Axis 2",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data["x"], y=data["y1"], mode="lines+markers", name="Y1", yaxis="y1"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data["x"], y=data["y2"], mode="lines+markers", name="Y2", yaxis="y2"
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis=dict(title=y_title1),
        yaxis2=dict(title=y_title2, overlaying="y", side="right"),
    )
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def grouped_bar_chart(
    data,
    title="Grouped Bar Chart",
    x_title="Categories",
    y_title="Values",
    orient="v",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    for group in data["groups"]:
        fig.add_trace(
            go.Bar(
                x=data["categories"],
                y=group["values"],
                name=group["name"],
                orientation=orient,
            )
        )
    fig.update_layout(
        title=title, xaxis_title=x_title, yaxis_title=y_title, barmode="group"
    )
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def heatmap(
    data,
    title="Heatmap",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
    colorscale=None
):
    fig = go.Figure(data=go.Heatmap(z=data["z"], x=data["x"], y=data["y"], colorscale=colorscale))
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def histogram(
    data,
    title="Histogram",
    x_title="Values",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(data=[go.Histogram(x=data["values"])])
    fig.update_layout(title=title, xaxis_title=x_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def line_chart(
    data,
    title="Line Chart",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(data=[go.Scatter(x=data["x"], y=data["y"], mode="lines+markers")])
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def multiline_chart(
    data,
    title="Multi-line Chart",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    for line in data["lines"]:
        fig.add_trace(
            go.Scatter(
                x=line["x"], y=line["y"], mode="lines+markers", name=line["name"]
            )
        )
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def pie_chart(
    data, title="Pie Chart", annotation=None, annotation_x=0.5, annotation_y=-0.2
):
    fig = go.Figure(data=[go.Pie(labels=data["labels"], values=data["values"])])
    fig.update_layout(title=title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def scatter_plot(
    data,
    title="Scatter Plot",
    x_title="X Axis",
    y_title="Y Axis",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure(data=[go.Scatter(x=data["x"], y=data["y"], mode="markers")])
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def simple_bar_chart(
    data,
    title="Simple Bar Chart",
    x_title="Values",
    y_title="Categories",
    orient="v",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
    reference_line=None,
):
    fig = go.Figure(
        data=[go.Bar(y=data["categories"], x=data["values"], orientation=orient)]
    )
    fig.update_layout(title=title, xaxis_title=x_title, yaxis_title=y_title)

    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )

    if reference_line:
        fig.add_shape(
            type="line",
            x0=reference_line,
            x1=reference_line,
            y0=0,
            y1=len(data["categories"]),
            line=dict(color="black", width=1, dash="dash"),
        )

    st.plotly_chart(fig)


def stacked_bar_chart(
    data,
    title="Stacked Bar Chart",
    x_title="Categories",
    y_title="Values",
    orient="v",
    annotation=None,
    annotation_x=0.5,
    annotation_y=-0.2,
):
    fig = go.Figure()
    for group in data["groups"]:
        fig.add_trace(
            go.Bar(
                x=data["categories"],
                y=group["values"],
                name=group["name"],
                orientation=orient,
            )
        )
    fig.update_layout(
        title=title, xaxis_title=x_title, yaxis_title=y_title, barmode="stack"
    )
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)


def sparkline_chart(
    data, title="Sparkline Chart", annotation=None, annotation_x=0.5, annotation_y=-0.2
):
    fig = go.Figure(data=[go.Scatter(x=data["x"], y=data["y"], mode="lines")])
    fig.update_layout(
        title=title,
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
    )
    if annotation:
        fig.add_annotation(
            text=annotation,
            xref="paper",
            yref="paper",
            x=annotation_x,
            y=annotation_y,
            showarrow=False,
        )
    st.plotly_chart(fig)
