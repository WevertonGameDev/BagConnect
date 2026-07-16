from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from services.auth_service import AuthService
from core.session import Session


class LoginScreen(MDScreen):

    auth = AuthService()


    def login(self):

        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()


        result = self.auth.login(
            email,
            password
        )


        if result:

            # Salva o usuário que acabou de logar
            Session.salvar_usuario(result)


            toast(
                App.get_running_app().tr(
                    "toast_login_realizado"
                )
            )


            self.manager.current = "home"


        else:

            toast(
                App.get_running_app().tr(
                    "toast_login_erro"
                )
            )



    def abrir_cadastro(self):

        self.manager.current = "register"