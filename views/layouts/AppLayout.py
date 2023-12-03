import dash
from views.partials.Sidebar import Sidebar
from views.partials.Footer import Footer
from dash import html

class AppLayout:
    @staticmethod
    def define_layout():
        return html.Div([
                Sidebar.define_layout(),
                html.Div([
                        html.Div(
                            html.Div(
                                html.Div(
                                    html.Div(
                                        dash.page_container,
                                        className='col-lg-12 mb-12',
                                    ),
                                    className='row',
                                ),
                                id='page-content',
                                className='container-fluid mar20'
                            ),
                            id = 'content',
                        ),
                        Footer.define_layout()
                    ],
                    id = 'content-wrapper',
                    className='d-flex flex-column'
                )
            ],
            id='wrapper',
        )