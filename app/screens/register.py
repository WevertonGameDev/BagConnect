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
                "Preencha todos os campos"
            )

            return


        if password != confirm:

            toast(
                "As senhas não conferem"
            )

            return


        result = self.auth.register(
            name,
            email,
            password
        )


        if result:

            toast(
                "Cadastro realizado"
            )

            self.manager.current = "login"


        else:

            toast(
                "Erro ao cadastrar"
            )



    def voltar_login(self):

        self.manager.current = "login"