import re

from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from services.auth_service import AuthService


class RegisterScreen(MDScreen):

    auth = AuthService()

    def validar_email(self, email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        return re.match(
            padrao,
            email
        ) is not None


    def validar_campos(self, *args):

        usuario = self.ids.name.text.strip()
        email = self.ids.email.text.strip()
        senha = self.ids.password.text
        confirmar = self.ids.confirm_password.text

        # Usuário
        self.ids.name.error = (
            usuario == ""
        )

        # Email
        self.ids.email.error = (
            email != ""
            and not self.validar_email(email)
        )

        # Senha curta
        senha_curta = (
            senha != ""
            and len(senha) < 6
        )

        # Senhas diferentes
        senhas_diferentes = (
            senha != ""
            and confirmar != ""
            and senha != confirmar
        )

        # Campo senha
        self.ids.password.error = (
            senha_curta
            or senhas_diferentes
        )

        # Campo confirmar senha
        self.ids.confirm_password.error = (
            senhas_diferentes
        )

        # Tudo válido?
        valido = (
            usuario != ""
            and self.validar_email(email)
            and len(senha) >= 6
            and confirmar != ""
            and senha == confirmar
        )

        self.ids.register_button.disabled = not valido


    def cadastrar(self):

        self.validar_campos()

        usuario = self.ids.name.text.strip()
        email = self.ids.email.text.strip()
        senha = self.ids.password.text
        confirmar = self.ids.confirm_password.text

        if (
            not usuario
            or not email
            or not senha
            or not confirmar
        ):

            toast(
                App.get_running_app().tr(
                    "toast_preencha_campos"
                )
            )

            return

        if not self.validar_email(email):

            toast(
                App.get_running_app().tr(
                    "toast_email_invalido"
                )
            )

            return

        if len(senha) < 6:

            toast(
                App.get_running_app().tr(
                    "toast_senha_curta"
                )
            )

            return

        if senha != confirmar:

            toast(
                App.get_running_app().tr(
                    "toast_senhas_nao_conferem"
                )
            )

            return

        resultado = self.auth.register(
            usuario,
            email,
            senha
        )

        if resultado:

            toast(
                App.get_running_app().tr(
                    "toast_cadastro_realizado"
                )
            )

            self.ids.name.text = ""
            self.ids.email.text = ""
            self.ids.password.text = ""
            self.ids.confirm_password.text = ""

            self.validar_campos()

            self.manager.current = "login"

        else:

            toast(
                App.get_running_app().tr(
                    "toast_erro_cadastrar"
                )
            )


    def mostrar_senha(self):
        self.ids.password.password = not self.ids.password.password


    def mostrar_confirmar_senha(self):
        self.ids.confirm_password.password = (
            not self.ids.confirm_password.password
        )


        def voltar_login(self):
            self.manager.current = "login"