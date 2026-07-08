from kivymd.app import MDApp
from kivy.lang import Builder

from core.manager import ScreenManager

from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen



class BagConnectApp(MDApp):


    def build(self):


        Builder.load_file(
            "kv/login.kv"
        )

        Builder.load_file(
            "kv/register.kv"
        )

        Builder.load_file(
            "kv/home.kv"
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


        return manager