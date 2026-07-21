from kivy.app import App
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel


class ChatScreen(MDScreen):

    titulo = StringProperty("")
    mensagem_auto = StringProperty("")
    digite = StringProperty("")
    enviar = StringProperty("")

    ticket_atual = None

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

        self.titulo = app.tr("ticket_chat")
        self.mensagem_auto = app.tr("ticket_msg_auto")
        self.digite = app.tr("ticket_digite")
        self.enviar = app.tr("enviar")


    def voltar(self):
        self.manager.current = "support"


    def enviar_mensagem(self):
        campo = self.ids.mensagem
        texto = campo.text.strip()


        if not texto:

            return

        mensagem = MDCard(
            orientation="vertical",
            adaptive_height=True,
            padding="12dp",
            radius=[16],
            size_hint_x=.8,
            pos_hint={
                "right": 1
            }

        )

        label = MDLabel(
            text=texto,
            adaptive_height=True
        )

        mensagem.add_widget(label)

        self.ids.mensagens.add_widget(
            mensagem
        )

        campo.text = ""