from dash import html

class Footer:
    @staticmethod
    def define_layout():
        return html.Footer(
            html.Div(
                html.Div(
                    html.Span([
                        'Derechos de autor © ',
                        html.A('Urbam', href='https://www.eafit.edu.co/urbam', target='_blank'),
                        ' 2023'
                    ]),
                    className='copyright text-center my-auto'
                ),
                className='container my-auto'
            ),
            className='sticky-footer bg-white',
        )