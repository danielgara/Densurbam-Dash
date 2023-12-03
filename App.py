import dash
import dash_bootstrap_components as dbc
from dash import Dash
from views.layouts.AppLayout import AppLayout
from views.pages.HomePage import HomePage
from views.pages.ControlPanelPage import ControlPanelPage
from views.pages.ByYearPage import ByYearPage
from views.pages.ByUnitPage import ByUnitPage
from views.pages.ByDemographicsPage import ByDemographicsPage

class App:
    def __init__(self):
        self.app = Dash(__name__, use_pages=True, pages_folder="views/pages")
        self.register_pages()
        self.set_app_layout()

    def register_pages(self):
        self.home_page = HomePage()
        dash.register_page(
            self.home_page.name, path=self.home_page.path, 
            layout=self.home_page.layout, title=self.home_page.title
        )

        self.control_panel_page = ControlPanelPage()
        dash.register_page(
            self.control_panel_page.name, path=self.control_panel_page.path, 
            layout=self.control_panel_page.layout, title=self.control_panel_page.title
        )

        self.by_unit_page = ByUnitPage()
        dash.register_page(
            self.by_unit_page.name, path=self.by_unit_page.path, 
            layout=self.by_unit_page.layout, title=self.by_unit_page.title
        )

        self.by_year_page = ByYearPage()
        dash.register_page(
            self.by_year_page.name, path=self.by_year_page.path, 
            layout=self.by_year_page.layout, title=self.by_year_page.title
        )

        self.by_demographics_page = ByDemographicsPage()
        dash.register_page(
            self.by_demographics_page.name, path=self.by_demographics_page.path, 
            layout=self.by_demographics_page.layout, title=self.by_demographics_page.title
        )

    def set_app_layout(self):
        self.app.layout = AppLayout.define_layout()

    def run_app(self):
        self.app.run_server(debug=True)

app = App()
app.run_app()