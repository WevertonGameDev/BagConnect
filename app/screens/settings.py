from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import (
    MDFlatButton,
    MDRaisedButton,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import (
    OneLineAvatarIconListItem,
    IconLeftWidget,
    IconRightWidget,
)

from kivy.properties import StringProperty


class SettingsScreen(MDScreen):

    idioma = StringProperty("System")
    tema = StringProperty("System")

    dialog = None

    idioma_temp = "System"
    tema_temp = "System"


    # IDIOMA
    def abrir_menu_idioma(self):
        self.idioma_temp = self.idioma

        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="5dp",
        )

        for opcao in ["System", "English", "Português"]:

            item = OneLineAvatarIconListItem(
                text=opcao,
                on_release=lambda x, o=opcao: self.selecionar_idioma(o),
            )

            item.add_widget(
                IconLeftWidget(
                    icon="translate"
                )
            )

            if opcao == self.idioma:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )

            layout.add_widget(item)

        self.dialog = MDDialog(
            title="Idioma",
            type="custom",
            content_cls=layout,
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                MDRaisedButton(
                    text="Salvar",
                    on_release=self.salvar_idioma,
                ),
            ],
        )

        self.dialog.open()

    def selecionar_idioma(self, idioma):
        self.idioma_temp = idioma

    def salvar_idioma(self, *args):
        self.idioma = self.idioma_temp
        self.dialog.dismiss()


    # TEMA
    def abrir_menu_tema(self):

        self.tema_temp = self.tema

        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="5dp",
        )

        for opcao in ["System", "Dark", "Light"]:

            item = OneLineAvatarIconListItem(
                text=opcao,
                on_release=lambda x, o=opcao: self.selecionar_tema(o),
            )

            item.add_widget(
                IconLeftWidget(
                    icon="theme-light-dark"
                )
            )

            if opcao == self.tema:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )

            layout.add_widget(item)

        self.dialog = MDDialog(
            title="Tema",
            type="custom",
            content_cls=layout,
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                MDRaisedButton(
                    text="Salvar",
                    on_release=self.salvar_tema,
                ),
            ],
        )

        self.dialog.open()

    def selecionar_tema(self, tema):
        self.tema_temp = tema


    def salvar_tema(self, *args):
        self.tema = self.tema_temp
        self.dialog.dismiss()


    def voltar(self):
        self.manager.current = "home"