from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty

from models.ticket import Ticket


class SupportScreen(MDScreen):
    """
    Tela principal do suporte.

    Responsável por listar todos os tickets do usuário.
    """

    tickets = ListProperty([])

    def on_pre_enter(self, *args):
        self.carregar_tickets()

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