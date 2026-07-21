from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import (
    MDFlatButton,
    MDRaisedButton,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.list import (
    OneLineAvatarIconListItem,
    IconLeftWidget,
    IconRightWidget,
)

from kivy.app import App
from kivy.properties import StringProperty


class SettingsScreen(MDScreen):

    texto_idioma = StringProperty("")
    texto_tema = StringProperty("")
    config_titulo = StringProperty("")
    config_linguagem = StringProperty("")
    config_tema = StringProperty("")

    idioma = StringProperty("System")
    tema = StringProperty("System")

    dialog = None

    idioma_temp = "System"
    tema_temp = "System"

    cards_idioma = []
    cards_tema = []


    def on_pre_enter(self):
        app = App.get_running_app()

        self.idioma = app.idioma
        self.tema = app.tema

        self.atualizar_textos()


    # IDIOMA
    def abrir_menu_idioma(self):

        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

        app = App.get_running_app()

        self.idioma_temp = self.idioma
        self.cards_idioma = []

        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="5dp",
        )

        opcoes = [
            ("System", app.tr("config_sistema", "Sistema")),
            ("English", "English"),
            ("Português", "Português"),
        ]

        for valor, texto in opcoes:

            card = MDCard(
                orientation="vertical",
                ripple_behavior=True,
                radius=[12],
                elevation=0,
                size_hint_y=None,
                height="50dp",
                md_bg_color=(
                    (0.86, 0.92, 1, 1)
                    if valor == self.idioma_temp
                    else app.theme_cls.bg_normal
                ),
            )

            item = OneLineAvatarIconListItem(
                text=texto,
                divider=None,
                on_release=lambda x, o=valor: self.selecionar_idioma(o),
            )

            item.add_widget(
                IconLeftWidget(icon="translate")
            )

            if valor == self.idioma_temp:
                item.add_widget(
                    IconRightWidget(icon="check")
                )

            card.add_widget(item)
            layout.add_widget(card)

            self.cards_idioma.append(
                (card, item, valor)
            )

        self.dialog = MDDialog(
            title=self.config_linguagem,
            type="custom",
            content_cls=layout,
            buttons=[
                MDFlatButton(
                    text=app.tr("cancelar"),
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                MDRaisedButton(
                    text=app.tr("salvar"),
                    on_release=self.salvar_idioma,
                ),
            ],
        )

        self.dialog.open()


    def selecionar_idioma(self, idioma):

        app = App.get_running_app()

        self.idioma_temp = idioma

        for card, item, opcao in self.cards_idioma:

            card.md_bg_color = (
                (0.86, 0.92, 1, 1)
                if opcao == idioma
                else app.theme_cls.bg_normal
            )

            while len(item.children) > 1:
                item.remove_widget(item.children[0])

            if opcao == idioma:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )


    def salvar_idioma(self, *args):
        self.idioma = self.idioma_temp

        app = App.get_running_app()
        app.aplicar_idioma(self.idioma)

        self.dialog.dismiss()
        self.atualizar_textos()


    # TEMA
    def abrir_menu_tema(self):
        self.tema_temp = self.tema
        self.cards_tema = []

        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="5dp",
        )

        for opcao in ["System", "Dark", "Light"]:
            card = MDCard(
                orientation="vertical",
                ripple_behavior=True,
                radius=[12],
                elevation=0,
                size_hint_y=None,
                height="50dp",
                md_bg_color=(
                    (0.86, 0.92, 1, 1)
                    if opcao == self.tema_temp
                    else (1, 1, 1, 1)
                ),
            )

            item = OneLineAvatarIconListItem(
                text=opcao,
                divider=None,
                on_release=lambda x, o=opcao: self.selecionar_tema(o),
            )

            item.add_widget(
                IconLeftWidget(
                    icon="theme-light-dark"
                )
            )

            if opcao == self.tema_temp:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )

            card.add_widget(item)
            layout.add_widget(card)

            self.cards_tema.append(
                (card, item, opcao)
            )

        self.dialog = MDDialog(
            title=self.config_tema,
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

        for card, item, opcao in self.cards_tema:
            card.md_bg_color = (
                (0.86, 0.92, 1, 1)
                if opcao == tema
                else (1, 1, 1, 1)
            )

            while len(item.children) > 1:
                item.remove_widget(item.children[0])

            if opcao == tema:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )


    def salvar_tema(self, *args):
        self.tema = self.tema_temp

        app = App.get_running_app()
        app.aplicar_tema(self.tema)

        self.dialog.dismiss()
        self.atualizar_textos()


    def voltar(self):
        self.manager.current = "home"
    

    def atualizar_textos(self):
        app = App.get_running_app()

        self.config_titulo = app.tr("config_titulo")
        self.config_linguagem = app.tr("config_linguagem")
        self.config_tema = app.tr("config_tema")

        # Idioma
        if self.idioma == "System":
            self.texto_idioma = app.tr("config_sistema")
        elif self.idioma == "English":
            self.texto_idioma = app.tr("config_ingles")
        else:
            self.texto_idioma = app.tr("config_portugues")

        # Tema
        if self.tema == "System":
            self.texto_tema = app.tr("config_sistema")
        elif self.tema == "Dark":
            self.texto_tema = app.tr("config_escuro")
        else:
            self.texto_tema = app.tr("config_claro")