from dash import html
from views.components.Breadcrumb import Breadcrumb

class HomePage:
    def __init__(self):
        self.name = 'Home'
        self.path = '/'
        self.title = 'Densurbam - Inicio'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': './'
            }
        ]
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])