from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
from views.components.Breadcrumb import Breadcrumb

class ByUnitPage:
    def __init__(self):
        self.name = 'ByUnit'
        self.path = '/by-unit-of-analysis'
        self.title = 'Densurbam - Consulta por unidad de análisis'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': 'Home'
            },
            {
                'title': 'Consulta por unidad de análisis',
                'route': self.name
            }
        ]

        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
        for col in df.columns:
            df[col] = df[col].astype(str)

        df['text'] = df['state'] + '<br>' + \
            'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
            'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
            'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

        fig = go.Figure(data=go.Choropleth(
            locations=df['code'],
            z=df['total exports'].astype(float),
            locationmode='USA-states',
            colorscale='Reds',
            autocolorscale=False,
            text=df['text'], 
            marker_line_color='white',
            colorbar_title="Millones USD"
        ))

        fig.update_layout(
            geo = dict(
                scope='usa',
                projection=go.layout.geo.Projection(type = 'albers usa'),
                showlakes=True,
                lakecolor='rgb(255, 255, 255)'),
            margin=dict(t=30, b=20)
        )

        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
            html.Div([
                    html.Div([
                            html.H6("Exportaciones de agricultura por estado (2021)", className="m-0 font-weight-bold text-primary")
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