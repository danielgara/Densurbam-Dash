import dash
from dash import html, dcc

class Breadcrumb:
    @staticmethod
    def define_layout(navigationList):
        items = [
            html.Li(
                item['title'] if index == len(navigationList)-1 else
                dcc.Link(
                    item['title'],
                    href=dash.page_registry[item['route']]['path'],
                ),
                className='breadcrumb-item',
            )
            for index, item in enumerate(navigationList)
        ]

        return html.Nav(
            html.Ol(
                [*items],
                className='breadcrumb'
                
            ),
            className='breadcrumb-font',
            **{'aria-label': 'breadcrumb'}
        )