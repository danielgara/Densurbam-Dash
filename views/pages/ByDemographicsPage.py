from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd
from views.components.Breadcrumb import Breadcrumb

class ByDemographicsPage:
    def __init__(self):
        self.name = 'ByDemographics'
        self.path = '/by-demographics'
        self.title = 'Densurbam - Consulta por demografía'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': 'Home'
            },
            {
                'title': 'Consulta por demografía',
                'route': self.name
            }
        ]

        # Load the data into a pandas DataFrame
        df = pd.read_csv("data/population_data.csv")

        # Create the male and female bar traces
        trace_male = go.Bar(x=df[df["gender"]=="M"]["count"],
                            y=df[df["gender"]=="M"]["age"],
                            orientation="h",
                            name="Hombres",
                            hoverinfo='x',
                            marker=dict(color="#1f77b4"),
                            base=0)

        trace_female = go.Bar(x=df[df["gender"]=="F"]["count"]*(-1),
                            y=df[df["gender"]=="F"]["age"],
                            orientation="h",
                            name="Mujeres",
                            hovertext=df[df["gender"]=="F"]["count"],
                            hoverinfo='text',
                            marker=dict(color="#d62728"))

        # Create the layout
        layout = go.Layout(xaxis=go.layout.XAxis(
                            range=[-120, 120],
                            tickvals=[-100, -70, -30, 0, 30, 70, 100],
                            ticktext=[100, 70, 30, 0, 30, 70, 100],
                            title='Cantidad'),
                        yaxis=dict(title="Edad"),
                        barmode="overlay",
                        bargap=0.1,
                        margin=dict(t=40, b=20))

        # Create the figure
        fig = go.Figure(data=[trace_male, trace_female], layout=layout)

        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
            html.Div([
                    html.Div([
                            html.H6("Piramide poblacional (2022)", className="m-0 font-weight-bold text-primary")
                        ],
                        className="card-header py-3"
                    ),
                    html.Div(
                        dcc.Graph(figure=fig),
                        className="card-body"
                    )
                ],
                className="card shadow mb-4",
            ),
        ])