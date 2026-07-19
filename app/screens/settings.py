from kivy.app import App

from kivymd.uix.screen import MDScreen


class SettingsScreen(MDScreen):

    idioma = StringProperty("System")
    tema = StringProperty("System")

    dialog = None

    idioma_temp = "System"
    tema_temp = "System"

    cards_idioma = []
    cards_tema = []


    # =========================
    # IDIOMA
    # =========================

    def abrir_menu_idioma(self):
        self.idioma_temp = self.idioma
        self.cards_idioma = []

        layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing="5dp",
        )

        for opcao in ["System", "English", "Português"]:

            card = MDCard(
                orientation="vertical",
                ripple_behavior=True,
                radius=[12],
                elevation=0,
                size_hint_y=None,
                height="50dp",
                md_bg_color=(
                    (0.86, 0.92, 1, 1)
                    if opcao == self.idioma_temp
                    else (1, 1, 1, 1)
                ),
            )

            item = OneLineAvatarIconListItem(
                text=opcao,
                divider=None,
                on_release=lambda x, o=opcao: self.selecionar_idioma(o),
            )

            item.add_widget(
                IconLeftWidget(
                    icon="translate"
                )
            )

            if opcao == self.idioma_temp:
                item.add_widget(
                    IconRightWidget(
                        icon="check"
                    )
                )

            card.add_widget(item)
            layout.add_widget(card)

            self.cards_idioma.append(
                (card, item, opcao)
            )

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

        for card, item, opcao in self.cards_idioma:

            card.md_bg_color = (
                (0.86, 0.92, 1, 1)
                if opcao == idioma
                else (1, 1, 1, 1)
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


    # =========================
    # TEMA
    # =========================

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


    def on_pre_enter(self, *args):

        app = App.get_running_app()

        self.modo_escuro = app.theme_cls.theme_style == "Dark"


    def selecionar_tema(self, tema):

        self.tema_temp = tema

        for card, item, opcao in self.cards_tema:

            card.md_bg_color = (
                (0.86, 0.92, 1, 1)
                if opcao == tema
                else (1, 1, 1, 1)
            )

        App.get_running_app().alternar_tema(ativo)

        self.modo_escuro = ativo


    def salvar_tema(self, *args):

        self.tema = self.tema_temp

        app = App.get_running_app()
        app.aplicar_tema(self.tema)

        self.dialog.dismiss()

    def voltar_home(self):

        self.manager.current = "home"