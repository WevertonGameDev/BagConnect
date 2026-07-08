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
                "Login realizado"
            )

            # futuro:
            # self.manager.current = "home"


        else:

            toast(
                "Informe email e senha"
            )



    def abrir_cadastro(self):

        self.manager.current = "register"