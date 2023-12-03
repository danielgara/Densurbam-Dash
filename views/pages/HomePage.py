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
                'route': 'Home'
            }
        ]
        self.layout = html.Div([
            Breadcrumb.define_layout(navigationList),
            html.Div([
                    html.Div([
                            html.H6("Urbam", className="m-0 font-weight-bold text-primary")
                        ],
                        className="card-header py-3"
                    ),
                    html.Div([
                            html.P([
                                "En urbam ",
                                html.Strong("creamos entornos urbanos y rurales sostenibles"),
                                " e incluyentes que buscan el bienestar humano."
                            ]),
                            html.P([
                                "Transformamos ",
                                html.Strong("territorios emergentes"),
                                " que se caracterizan por procesos acelerados de cambio, con problemáticas, urbanas y ambientales de alta complejidad en el contexto de la región tropical."
                            ]),
                            html.P([
                                "Nacimos para ",
                                html.Strong("conectar la academia con el mundo real"),
                                ". Como ",
                                html.Strong("espacio de mediación"),
                                " entre la universidad, las instituciones y las comunidades. Como centro de investigación y creación ",
                                html.Strong("hacia la incidencia"),
                                "."
                            ]),
                            html.P([
                                "Nuestro foco son los problemas reales, teniendo como ",
                                html.Strong("centro las personas"),
                                "."
                            ])
                        ],
                        className="card-body"
                    )
                ],
                className="card shadow mb-4",
            ),
            html.Div([
                    html.Div([
                            html.H6("Densurbam", className="m-0 font-weight-bold text-primary")
                        ],
                        className="card-header py-3"
                    ),
                    html.Div([
                            html.P("Densurbam es un modelo para analizar las capacidades de soporte de una ciudad-territorio, "
                                "teniendo en cuenta criterios estratégicos de sostenibilidad. El modelo permite calcular un "
                                "índice de relación de soporte a partir de la relación existente entre la demanda poblacional " 
                                "de un recurso natural o urbano especifico y la determinación de las ofertas natural y urbanas, "
                                "contrastando con límites denominados umbrales de sostenibilidad, asociados al capital natural "
                                "y al capital urbano y social. El valor del índice cambia en el tiempo y permite establecer "
                                "para un horizonte temporal definido, el momento en el cual se alcanza el umbral de sostenibilidad, "
                                "entendido como el momento a partir del cual la oferta del recurso no es suficiente para atender "
                                "la demanda de la población de dicho recurso."),
                            html.P("El modelo Densurbam es paramétrico y está basado en la población que habita los territorios, "
                                "en este caso fue contratado por el Área Metropolitana del Valle de Aburrá para realizar el "
                                "estudio en los 10 municipios que la componen, ha sido planteado desde las unidades de análisis "
                                "y las posibilidades que estas ofrecen para operar variables ambientales, sociales y urbanas. "
                                "El centro del modelo es la población, su densidad por unidad territorial y la demanda que esta "
                                "genera de servicios públicos, sociales y ambientales. "),
                            html.P("El modelo permite simular diferentes escenarios de crecimiento poblacional, sus efectos sobre "
                                "el sistema urbano-ambiental y las modificaciones a la capacidad de soporte a través de las "
                                "formas de ocupación y/o de consumo, denominadas, como se ha mencionado, habilidades sociales "
                                "para el desarrollo. "),
                            html.P([
                                    html.Img(
                                        alt="Logo",
                                        className="img-fluid width-400",
                                        id="logo",
                                        src="./assets/images/logo-densurbam.jpeg",
                                    )
                                ],
                                className="text-center"
                            ) 
                            
                        ],
                        className="card-body"
                    )
                ],
                className="card shadow mb-4",
            )
        ])

        