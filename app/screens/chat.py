from kivymd.uix.screen import MDScreen


class ChatScreen(MDScreen):

    def voltar(self):
        self.manager.current = "support"

    def enviar_mensagem(self):
        pass