from dash import html
from views.components.Breadcrumb import Breadcrumb

class AnalyticsPage:
    def __init__(self):
        self.name = 'Analytics'
        self.path = '/analytics'
        self.title = 'Densurbam - Analíticas'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': './'
            },
            {
                'title': 'Analíticas',
                'route': self.path
            }
        ]
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])