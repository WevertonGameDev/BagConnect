from kivymd.uix.screen import MDScreen
from kivy.animation import Animation

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from services.bag_service import BagService


class FindBagsScreen(MDScreen):

    dialog = None


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
                "Atenção",
                "Preencha o CPF e o código da bagagem."
            )
            return

        bagagem = BagService.buscar_bagagem(
            cpf,
            codigo
        )

        if bagagem is None:

            self.ocultar_resultado()

            self.mostrar_dialogo(
                "Bagagem não encontrada",
                "Não foi encontrada nenhuma bagagem para os dados informados."
            )

            return

        self.mostrar_resultado(bagagem)


    # RESULTADO
    def mostrar_resultado(self, bagagem):

        self.ids.bag_codigo.text = (
            f"# Bag {bagagem['codigo']}"
        )

        self.ids.bag_status.text = (
            f"Status: {bagagem['status']}"
        )

        self.ids.bag_descricao.text = (
            "Bagagem localizada com sucesso."
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
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )

        self.dialog.open()