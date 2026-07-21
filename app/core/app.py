from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import NumericProperty

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
from screens.new_ticket import NewTicketScreen
from screens.chat import ChatScreen

from widgets.drawer import Drawer
from widgets.ticket_card import TicketCard


class BagConnectApp(MDApp):

    # Sempre que esse número mudar, todas as telas poderão atualizar seus textos.
    idioma_evento = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tradutor = Tradutor()

        self.tema = "System"
        self.idioma = "System"


    # Tradução
    def tr(self, chave, valor_padrao=None):
        return self.tradutor.traduzir(chave, valor_padrao)


    # Tema
    def aplicar_tema(self, tema):

        self.tema = tema

        if tema == "Dark":
            self.theme_cls.theme_style = "Dark"

        elif tema == "Light":
            self.theme_cls.theme_style = "Light"

        else:
            self.theme_cls.theme_style = System.detectar_tema()

    # Idioma
    def aplicar_idioma(self, idioma):

        self.idioma = idioma

        if idioma == "English":
            self.tradutor.idioma = "en"

        elif idioma == "Português":
            self.tradutor.idioma = "pt"

        else:
            self.tradutor.idioma = System.detectar_idioma()

        # Dispara um evento para todas as telas
        self.idioma_evento += 1


    # Build
    def build(self):

        Builder.load_file("widgets/drawer.kv")
        Builder.load_file("widgets/ticket_card.kv")

        Builder.load_file("kv/login.kv")
        Builder.load_file("kv/register.kv")
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/profile.kv")
        Builder.load_file("kv/find_bags.kv")
        Builder.load_file("kv/settings.kv")
        Builder.load_file("kv/support.kv")
        Builder.load_file("kv/new_ticket.kv")
        Builder.load_file("kv/chat.kv")

        self.theme_cls.primary_palette = "Blue"

        self.aplicar_tema(self.tema)

        manager = ScreenManager()

        manager.add_widget(LoginScreen(name="login"))
        manager.add_widget(RegisterScreen(name="register"))
        manager.add_widget(HomeScreen(name="home"))
        manager.add_widget(ProfileScreen(name="profile"))
        manager.add_widget(FindBagsScreen(name="find_bags"))
        manager.add_widget(SettingsScreen(name="settings"))
        manager.add_widget(SupportScreen(name="support"))
        manager.add_widget(NewTicketScreen(name="new_ticket"))
        manager.add_widget(ChatScreen(name="chat"))

        return manager