from dash import html
from views.components.Breadcrumb import Breadcrumb

class ByYearPage:
    def __init__(self):
        self.name = 'ByYear'
        self.path = '/by-year'
        self.title = 'Densurbam - Consulta por año'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': './'
            },
            {
                'title': 'Consulta por año',
                'route': self.path
            }
        ]
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])