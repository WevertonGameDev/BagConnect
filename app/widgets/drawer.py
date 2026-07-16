from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


class Drawer(MDBoxLayout):

    nome = StringProperty("Usuário")

    email = StringProperty("usuario@email.com")

    foto = StringProperty("assets/images/avatar_default.png")