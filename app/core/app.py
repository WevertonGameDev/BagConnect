from kivymd.app import MDApp
from kivy.lang import Builder

from core.manager import ScreenManager
from core.idioma import Tradutor 

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen
from screens.profile import ProfileScreen

from widgets.drawer import Drawer


class BagConnectApp(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tradutor = Tradutor()


    def tr(self, chave, valor_padrao=None):
        return self.tradutor.traduzir(chave, valor_padrao)


    def build(self):

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

        self.theme_cls.primary_palette = "Blue"

        self.theme_cls.theme_style = "Light"



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

        return manager