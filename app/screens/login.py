from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from services.auth_service import AuthService



class LoginScreen(MDScreen):


    auth = AuthService()



    def login(self):

        email = self.ids.email.text
        password = self.ids.password.text


        result = self.auth.login(
            email,
            password
        )


        if result:

            toast(
                App.get_running_app().tr("toast_login_realizado")
            )


            self.manager.current = "home"

            # futuro:
            # self.manager.current = "home"


        else:

            toast(
                App.get_running_app().tr("toast_login_erro")
            )



    def abrir_cadastro(self):

        self.manager.current = "register"