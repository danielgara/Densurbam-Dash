from dash import html, dcc, callback, Output, Input, dash_table
from views.components.Breadcrumb import Breadcrumb
import plotly.express as px
import pandas as pd


class ByYearPage:
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

    def __init__(self):
        self.name = 'ByYear'
        self.path = '/by-year'
        self.title = 'Densurbam - Consulta por año'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': 'Home'
            },
            {
                'title': 'Consulta por año',
                'route': self.name
            }
        ]

        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.H6("Población de distintos países por año", className="m-0 font-weight-bold text-primary"),
                        ], className="card-header py-3"),
                        html.Div([
                            dcc.Dropdown(
                                options=[{'label': country, 'value': country} for country in ByYearPage.df['country'].unique()],
                                value='Afghanistan',
                                id='dropdown-selection'
                            ),
                            dcc.Graph(id='graph-content')
                        ], className="card-body"),
                    ], className="card shadow mb-4"),
                ], className="col-xl-6 col-lg-6"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.H6("Tabla de población por país y año", className="m-0 font-weight-bold text-primary"),
                        ], className="card-header py-3"),
                        html.Div([
                            dash_table.DataTable(
                                data=ByYearPage.df.to_dict('records'),
                                columns=[
                                    {'name': 'País', 'id': 'country'},
                                    {'name': 'Año', 'id': 'year'},
                                    {'name': 'Población', 'id': 'pop'}
                                ],
                                page_size=13,
                                style_cell={'textAlign': 'left'}
                            )
                        ], className="card-body"),
                    ], className="card shadow mb-4"),
                ], className="col-xl-6 col-lg-6"),
            ], className="row"),
        ])

    @callback(
        Output('graph-content', 'figure'),
        Input('dropdown-selection', 'value')
    )
    def update_graph(value):
        dff = ByYearPage.df[ByYearPage.df.country == value]
        fig = px.line(dff, x='year', y='pop')

        fig.update_layout(
            xaxis_title='Año',
            yaxis_title='Población',
        )
        return fig
