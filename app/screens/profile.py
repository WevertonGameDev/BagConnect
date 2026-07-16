from kivymd.uix.screen import MDScreen
from kivy.properties import (
    StringProperty,
    BooleanProperty
)

from core.session import Session


class ProfileScreen(MDScreen):

    usuario = StringProperty("")
    email = StringProperty("")
    foto = StringProperty(
        "assets/images/avatar_default.png"
    )

    conectado = BooleanProperty(False)

    def on_enter(self):
        user = Session.obter_usuario()

        if not user:
            return

        self.usuario = user.usuario
        self.email = user.email

        self.verificar_passageiro()


    def verificar_passageiro(self):
        """
        Consulta no banco se existe passageiro
        vinculado ao usuário.
        """
        pass


    def conectar_passageiro(self):
        """
        Abre popup para Nome Completo + CPF
        """
        pass


    def desconectar_passageiro(self):
        """
        Confirma desconexão
        """
        pass


    def editar_perfil(self):
        pass

    def voltar(self):
        self.manager.current = "home"