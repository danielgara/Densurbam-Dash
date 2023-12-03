from dash import html
from views.components.Breadcrumb import Breadcrumb

class ControlPanelPage:
    def __init__(self):
        self.name = 'ControlPanel'
        self.path = '/control-panel'
        self.title = 'Densurbam - Panel de control'
        self.set_layout()

    def set_layout(self):
        navigationList = [
            {
                'title': 'Inicio',
                'route': 'Home'
            },
            {
                'title': 'Panel de control',
                'route': self.path
            }
        ]
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
        ])