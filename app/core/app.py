from kivymd.app import MDApp
from kivy.lang import Builder

from core.manager import ScreenManager
from core.idioma import Tradutor
from core.system import System

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen
from screens.settings import SettingsScreen
from screens.profile import ProfileScreen
from screens.find_bags import FindBagsScreen
from screens.support import SupportScreen

from widgets.drawer import Drawer


class BagConnectApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tradutor = Tradutor()

        # Configurações atuais do usuário
        self.tema = "System"
        self.idioma = "System"

    def tr(self, chave, valor_padrao=None):
        return self.tradutor.traduzir(chave, valor_padrao)

    def aplicar_tema(self, tema):

        self.tema = tema

        if tema == "Dark":
            self.theme_cls.theme_style = "Dark"

        elif tema == "Light":
            self.theme_cls.theme_style = "Light"

        else:
            # System
            self.theme_cls.theme_style = System.detectar_tema()

    def aplicar_idioma(self, idioma):
        self.idioma = idioma

        if idioma == "English":
            self.tradutor.idioma = "en"

        elif idioma == "Português":
            self.tradutor.idioma = "pt"

        else:
            # Detecta automaticamente a linguagem do sistema
            self.tradutor.idioma = System.detectar_idioma()

        # Atualiza todas as telas já carregadas
        self.root.canvas.ask_update()

    def build(self):
        Builder.load_file("widgets/drawer.kv")
        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/register.kv")
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/profile.kv")
        Builder.load_file("kv/find_bags.kv")
        Builder.load_file("kv/settings.kv")
        Builder.load_file("kv/support.kv")

        self.theme_cls.primary_palette = "Blue"

        # Aplica o tema inicial
        self.aplicar_tema(self.tema)

        manager = ScreenManager()

        manager.add_widget(
            LoginScreen(
                name="login"
            )
        )

        manager.add_widget(
            RegisterScreen(
                name="register"
            )
        )

        manager.add_widget(
            HomeScreen(
                name="home"
            )
        )

        manager.add_widget(
            ProfileScreen(
                name="profile"
            )
        )

        manager.add_widget(
            FindBagsScreen(
                name="find_bags"
            )
        )

        manager.add_widget(
            SettingsScreen(
                name="settings"
            )
        )

        manager.add_widget(
            SupportScreen(
                name="support"
            )
        )

        return manager