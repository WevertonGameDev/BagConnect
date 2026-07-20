from kivymd.uix.screen import MDScreen


class SupportScreen(MDScreen):

    def voltar(self):
        self.manager.current = "home"

    def novo_ticket(self):
        print("Novo Ticket")