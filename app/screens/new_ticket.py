from kivymd.uix.screen import MDScreen
from kivymd.toast import toast


class NewTicketScreen(MDScreen):

    def voltar(self):
        self.manager.current = "support"

    def criar_ticket(self):

        assunto = self.ids.assunto
        descricao = self.ids.descricao
        cpf = self.ids.cpf
        codigo = self.ids.codigo

        campos = [
            assunto,
            descricao,
            cpf,
            codigo
        ]

        valido = True

        # Limpa os erros anteriores
        for campo in campos:
            campo.error = False

        # Verifica todos os campos
        for campo in campos:

            if not campo.text.strip():

                campo.error = True
                valido = False

        if not valido:

            toast(
                "Preencha todos os campos."
            )

            return

        # Aqui depois iremos salvar no banco

        self.manager.current = "chat"