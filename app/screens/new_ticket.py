from kivy.app import App
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.toast import toast


class NewTicketScreen(MDScreen):


    titulo = StringProperty("")
    descricao_ticket = StringProperty("")
    assunto = StringProperty("")
    descricao_label = StringProperty("")
    cpf = StringProperty("")
    codigo_bagagem = StringProperty("")
    criar = StringProperty("")
    campo_obrigatorio = StringProperty("")


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


        self.titulo = app.tr("novo_ticket")
        self.descricao_ticket = app.tr("ticket_descricao")
        self.assunto = app.tr("ticket_assunto")
        self.descricao_label = app.tr("ticket_descricao_label")
        self.cpf = app.tr("ticket_cpf")
        self.codigo_bagagem = app.tr("ticket_codigo")
        self.criar = app.tr("ticket_criar")
        self.campo_obrigatorio = app.tr("campo_obrigatorio")


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
            toast(App.get_running_app().tr("campo_obrigatorio"))

            return

        # Aqui depois iremos salvar no banco

        self.manager.current = "chat"