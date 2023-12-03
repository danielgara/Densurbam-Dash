from dash import html

class Breadcrumb:
    @staticmethod
    def define_layout(navigationList):
        items = [
            html.Li(
                item['title'] if index == len(navigationList)-1 else
                html.A(
                    item['title'],
                    href=item['route']
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