from dash import html
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
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])