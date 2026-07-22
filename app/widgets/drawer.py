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

    menu_home = StringProperty("")
    menu_bagagens = StringProperty("")
    menu_suporte = StringProperty("")
    menu_perfil = StringProperty("")
    menu_configuracoes = StringProperty("")
    menu_sair = StringProperty("")


    def on_kv_post(self, base_widget):
        self.atualizar_textos()
        self.carregar_usuario()


    def carregar_usuario(self):
        usuario = Session.obter_usuario()

        if usuario:
            self.nome = usuario.usuario
            self.email = usuario.email


        else:
            app = App.get_running_app()

            self.nome = app.tr("home_usuario_padrao")
            self.email = ""

            self.foto = "assets/images/avatar_default.png"
    

    def abrir_home(self):
        App.get_running_app().root.current = "home"


    def abrir_perfil(self):
        App.get_running_app().root.current = "profile"


    def abrir_bagagens(self):
        App.get_running_app().root.current = "find_bags"


    def abrir_suporte(self):
        App.get_running_app().root.current = "support"



    def sair(self):
        # Limpa a sessão
        Session.salvar_usuario(None)

        app = App.get_running_app()

        # Fecha o menu
        try:
            app.root.get_screen("home").fechar_menu()
        except:
            pass

        # Limpa os campos de login
        login = app.root.get_screen("login")

        login.ids.email.text = ""
        login.ids.password.text = ""

        # Atualiza o drawer para o usuário padrão
        self.carregar_usuario()

        # Vai para login
        app.root.current = "login"

    
    def atualizar_textos(self):
        app = App.get_running_app()

        self.menu_home = app.tr("menu_home")
        self.menu_bagagens = app.tr("menu_bagagens")
        self.menu_suporte = app.tr("menu_suporte")
        self.menu_perfil = app.tr("menu_perfil")
        self.menu_configuracoes = app.tr("menu_configuracoes")
        self.menu_sair = app.tr("menu_sair")