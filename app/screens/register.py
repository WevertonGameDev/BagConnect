from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from services.auth_service import AuthService


class RegisterScreen(MDScreen):


    auth = AuthService()


    def cadastrar(self):

        name = self.ids.name.text
        email = self.ids.email.text
        password = self.ids.password.text
        confirm = self.ids.confirm_password.text


        if not name or not email or not password:

            toast(
                App.get_running_app().tr("toast_preencha_campos")
            )

            return


        if password != confirm:

            toast(
                App.get_running_app().tr("toast_senhas_nao_conferem")
            )

            return


        result = self.auth.register(
            name,
            email,
            password
        )


        if result:

            toast(
                App.get_running_app().tr("toast_cadastro_realizado")
            )

            self.manager.current = "login"


        else:

            toast(
                App.get_running_app().tr("toast_erro_cadastrar")
            )



    def voltar_login(self):

        self.manager.current = "login"