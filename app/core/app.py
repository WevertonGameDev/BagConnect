from kivymd.app import MDApp
from kivy.lang import Builder

from core.manager import ScreenManager
from core.idioma import Tradutor

from services.theme_service import ThemeService

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen
from screens.settings import SettingsScreen
from screens.profile import ProfileScreen
from screens.find_bags import FindBagsScreen
from screens.settings import SettingsScreen

from widgets.drawer import Drawer


class BagConnectApp(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tradutor = Tradutor()
        self.theme_service = ThemeService()


    def tr(self, chave, valor_padrao=None):
        return self.tradutor.traduzir(chave, valor_padrao)


    def alternar_tema(self, escuro):

        self.theme_cls.theme_style = "Dark" if escuro else "Light"

        self.theme_service.salvar_tema(self.theme_cls.theme_style)


    def build(self):

        self.theme_cls.primary_palette = "Blue"

        # Aplica o tema salvo ANTES de carregar as telas
        self.theme_cls.theme_style = self.theme_service.carregar_tema()


        Builder.load_file(
            "widgets/drawer.kv"
        )

        Builder.load_file(
            "kv/login.kv"
        )

        Builder.load_file(
            "kv/register.kv"
        )

        Builder.load_file(
            "kv/home.kv"
        )

        Builder.load_file(
            "kv/profile.kv"
        )

        Builder.load_file(
            "kv/find_bags.kv"
        )

        Builder.load_file(
            "kv/settings.kv"
        )


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

        return manager