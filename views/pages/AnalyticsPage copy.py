from dash import html, dcc, callback, Input, Output

class AnalyticsPage:
    def __init__(self):
        self.name = 'Analytics'
        self.path = '/analytics'
        self.title = 'Densurbam - Analíticas'
        self.set_layout()

    def set_layout(self):
        self.layout = html.Div([
            html.H1('This is our Analytics page'),
            html.Div([
                "Select a city: ",
                dcc.RadioItems(
                    options=['New York City', 'Montreal', 'San Francisco'],
                    value='Montreal',
                    id='analytics-input',
                    persistence=True,
                )
            ]),
            html.Br(),
            html.Div(id='analytics-output'),
        ])

    @callback(
        Output('analytics-output', 'children'),
        Input('analytics-input', 'value')
    )
    def update_city_selected(input_value):
        return 'You selected: '+input_value