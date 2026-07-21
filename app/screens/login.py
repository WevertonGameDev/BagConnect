from kivy.app import App
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from services.auth_service import AuthService
from core.session import Session


class LoginScreen(MDScreen):

    auth = AuthService()

    titulo_app = StringProperty("")
    subtitulo = StringProperty("")
    titulo_login = StringProperty("")
    email = StringProperty("")
    senha = StringProperty("")
    botao_login = StringProperty("")
    criar_conta = StringProperty("")
    rodape = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = App.get_running_app()

        if app:
            app.bind(idioma_evento=self._idioma_alterado)

    def on_kv_post(self, base_widget):
        self.atualizar_textos()

    def _idioma_alterado(self, *args):
        self.atualizar_textos()

    def atualizar_textos(self):

        app = App.get_running_app()

        self.titulo_app = app.tr("app_nome")
        self.subtitulo = app.tr("login_subtitulo")
        self.titulo_login = app.tr("login_titulo")
        self.email = app.tr("campo_email")
        self.senha = app.tr("campo_senha")
        self.botao_login = app.tr("login_botao")
        self.criar_conta = app.tr("criar_conta")
        self.rodape = app.tr("rodape_app")

    def login(self):

        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        result = self.auth.login(email, password)

        if result:

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