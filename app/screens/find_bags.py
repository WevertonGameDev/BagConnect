from kivy.app import App
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivy.animation import Animation

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from services.bag_service import BagService


class FindBagsScreen(MDScreen):
    dialog = None

    titulo = StringProperty("")

    cpf_titulo = StringProperty("")
    cpf_hint = StringProperty("")
    cpf_helper = StringProperty("")

    codigo_titulo = StringProperty("")
    codigo_hint = StringProperty("")
    codigo_helper = StringProperty("")

    botao_consultar = StringProperty("")

    resultado_titulo = StringProperty("")
    status_label = StringProperty("")


    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        app = App.get_running_app()

        if app:

            app.bind(
                idioma_evento=self._idioma_alterado
            )


    def on_pre_enter(self):

        self.atualizar_textos()


    def _idioma_alterado(self, *args):

        self.atualizar_textos()


    def atualizar_textos(self):
        app = App.get_running_app()

        self.titulo = app.tr("find_bags_titulo")
        self.cpf_titulo = app.tr("find_bags_cpf")
        self.cpf_hint = app.tr("find_bags_cpf_hint")
        self.cpf_helper = app.tr("find_bags_cpf_helper")
        self.codigo_titulo = app.tr("find_bags_codigo")
        self.codigo_hint = app.tr("find_bags_codigo_hint")
        self.codigo_helper = app.tr("find_bags_codigo_helper")
        self.botao_consultar = app.tr("find_bags_botao_consultar")
        self.resultado_titulo = app.tr("find_bags_encontrada")
        self.status_label = app.tr("find_bags_status")


    # BOTÕES
    def voltar(self):
        self.manager.current = "home"


    def abrir_historico(self):
        print("Abrir histórico")


    # CONSULTA
    def consultar_bagagem(self):

        cpf = self.ids.cpf.text.strip()
        codigo = self.ids.codigo.text.strip()

        if not cpf or not codigo:
            self.mostrar_dialogo(

                App.get_running_app().tr(
                    "find_bags_atencao"
                ),

                App.get_running_app().tr(
                    "find_bags_preencha_campos"
                )
            )
            return

        bagagem = BagService.buscar_bagagem(
            cpf,
            codigo
        )

        if bagagem is None:

            self.ocultar_resultado()

            self.mostrar_dialogo(

                App.get_running_app().tr(
                    "find_bags_nao_encontrada"
                ),

                App.get_running_app().tr(
                    "find_bags_nao_encontrada_texto"
                )
            )

            return

        self.mostrar_resultado(bagagem)


    # RESULTADO
    def mostrar_resultado(self, bagagem):

        self.ids.bag_codigo.text = (
            f"# Bag {bagagem['codigo']}"
        )

        self.ids.bag_status.text = (

            f"{App.get_running_app().tr('find_bags_status_prefix')} "
            f"{bagagem['status']}"

        )

        self.ids.bag_descricao.text = (

            App.get_running_app().tr(
                "find_bags_resultado_sucesso"
            )

        )

        card = self.ids.resultado_card

        card.disabled = False

        Animation(
            opacity=1,
            d=.25
        ).start(card)


    def ocultar_resultado(self):

        card = self.ids.resultado_card

        Animation(
            opacity=0,
            d=.25
        ).start(card)

        card.disabled = True


    # DIALOG
    def mostrar_dialogo(
        self,
        titulo,
        texto
    ):

        if self.dialog:
            self.dialog.dismiss()

        self.dialog = MDDialog(
            title=titulo,
            text=texto,
            buttons=[
                MDFlatButton(
                    text=App.get_running_app().tr("find_bags_ok"),
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )

        self.dialog.open()