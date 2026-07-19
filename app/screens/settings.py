from kivy.app import App
from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen


class SettingsScreen(MDScreen):

    modo_escuro = BooleanProperty(False)


    def on_pre_enter(self, *args):

        app = App.get_running_app()

        self.modo_escuro = app.theme_cls.theme_style == "Dark"


    def alternar_tema(self, ativo):

        App.get_running_app().alternar_tema(ativo)

        self.modo_escuro = ativo


    def voltar_home(self):

        self.manager.current = "home"