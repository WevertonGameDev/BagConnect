from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App

from core.session import Session


class Drawer(MDBoxLayout):
    nome = StringProperty("")
    email = StringProperty("")
    foto = StringProperty(
        "assets/images/avatar_default.png"
    )


    def on_kv_post(self, base_widget):
        self.carregar_usuario()


    def carregar_usuario(self):
        usuario = Session.obter_usuario()

        if usuario:
            self.nome = usuario.usuario
            self.email = usuario.email


        else:
            app = App.get_running_app()
            self.nome = app.tr(
                "home_usuario_padrao"
            )

            self.email = ""