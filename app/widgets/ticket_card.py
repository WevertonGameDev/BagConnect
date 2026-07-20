from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty


class TicketCard(MDCard):
    ticket = ObjectProperty()
    screen = ObjectProperty()

    def abrir(self):
        self.screen.abrir_ticket(self.ticket)