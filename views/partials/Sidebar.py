import dash
from dash import html, dcc, callback, Input, Output, State

class Sidebar:
    @staticmethod
    def define_layout():
        return html.Ul([
                html.A([
                        html.Div('D', className='sidebar-brand-icon rotate-n-15 display-icon', id='main-icon'),
                        html.Div('Densurbam', className='sidebar-brand-text mx-3')
                    ],
                    className='sidebar-brand d-flex align-items-center justify-content-center',
                    href=dash.page_registry['Home']['path'],
                ),
                html.Hr(className='sidebar-divider my-0 hr-nav-top'),
                html.Li(
                    dcc.Link([
                            html.I(className='fas fa-fw fa-home'),
                            html.Span('Inicio'),
                        ],
                        href=dash.page_registry['Home']['path'],
                        className='router-link-active router-link-exact-active nav-link'
                    ),
                    className='nav-item'
                ),
                html.Li(
                    dcc.Link([
                            html.I(className='fas fa-fw fa-info-circle'),
                            html.Span('Analíticas'),
                        ],
                        href=dash.page_registry['Analytics']['path'],
                        className='router-link-active router-link-exact-active nav-link'
                    ),
                    className='nav-item'
                ),
                html.Hr(className='sidebar-divider my-0 hr-nav-bottom'),
                html.Div(
                    html.Button(className='rounded-circle border-0', id='sidebarToggle'),
                    className='text-center d-none d-md-inline',
                )
            ],
            className='navbar-nav sidebar sidebar-dark accordion',
            id='accordionSidebar'
        )

    @callback(
        Output('accordionSidebar', 'className'),
        Output('main-icon', 'className'),
        Input('sidebarToggle', 'n_clicks'),
        State('accordionSidebar', 'className'),
        State('main-icon', 'className')
    )
    def toggle_classes(n_clicks, accordionSidebar_class, main_icon_class):
        if n_clicks is None:
            return dash.no_update, dash.no_update
        
        sidebar_ne = 'toggled'
        sidebar_new = accordionSidebar_class
        if sidebar_ne not in sidebar_new:
            sidebar_new = sidebar_new + ' ' + sidebar_ne
        else:
            sidebar_new = 'navbar-nav sidebar sidebar-dark accordion'

        main_icon_ne = 'display-icon-yes'
        main_icon_new = str(main_icon_class)
        if main_icon_ne not in main_icon_class:
            main_icon_new = main_icon_new + ' ' + main_icon_ne
        else:
            main_icon_new = 'sidebar-brand-icon rotate-n-15 display-icon'

        return sidebar_new, main_icon_new.strip()