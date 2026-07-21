from kivy.app import App
from kivy.properties import ListProperty, StringProperty

from kivymd.uix.screen import MDScreen

from models.ticket import Ticket


class SupportScreen(MDScreen):
    """
    Tela principal do suporte.

    Responsável por listar todos os tickets do usuário.
    """

    tickets = ListProperty([])

    titulo = StringProperty("")
    novo_ticket = StringProperty("")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        app = App.get_running_app()

        if app:
            app.bind(
                idioma_evento=self._idioma_alterado
            )


    def on_pre_enter(self, *args):
        self.atualizar_textos()
        self.carregar_tickets()


    def _idioma_alterado(self, *args):
        self.atualizar_textos()


    def atualizar_textos(self):

        app = App.get_running_app()

        self.titulo = app.tr(
            "menu_suporte"
        )

        self.novo_ticket = app.tr(
            "suporte_novo_ticket"
        )


    def carregar_tickets(self):
        """
        Futuramente será substituído pelo banco.

        Ex:
            self.tickets = TicketDAO.listar(usuario_id)

        Por enquanto apenas mantém a lista em memória.
        """
        self.tickets = Ticket.lista


    def abrir_novo_ticket(self):
        self.manager.current = "new_ticket"

    def abrir_ticket(self, ticket):
        """
        Guarda o ticket selecionado para o Chat.
        """

        from screens.chat import ChatScreen

        ChatScreen.ticket_atual = ticket

        self.manager.current = "chat"


    def atualizar_lista(self):
        self.carregar_tickets()