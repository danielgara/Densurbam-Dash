from dash import html
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
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])