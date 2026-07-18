from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.animation import Animation

from core.session import Session


class HomeScreen(MDScreen):

    nome_usuario = StringProperty("")
    email_usuario = StringProperty("")

    menu_aberto = False

    # CARREGAR USUÁRIO LOGADO
    def on_enter(self):
        usuario = Session.obter_usuario()

        if usuario:
            self.nome_usuario = usuario.usuario
            self.email_usuario = usuario.email
            
        else:
            self.nome_usuario = App.get_running_app().tr("home_usuario_padrao")
            self.email_usuario = App.get_running_app().tr("home_email_padrao")
        
        self.ids.drawer.carregar_usuario()

    # MENU
    def abrir_menu(self):
        if self.menu_aberto:
            return

        drawer = self.ids.drawer
        overlay = self.ids.overlay

        # ativa o drawer para receber toque
        drawer.disabled = False

        overlay.disabled = False

        overlay.size_hint = (1, 1)
        overlay.size = self.size

        Animation(
            x=0,
            d=.25,
            t="out_cubic"
        ).start(drawer)

        Animation(
            opacity=1,
            d=.25
        ).start(overlay)

        self.menu_aberto = True


    def fechar_menu(self):

        if not self.menu_aberto:
            return

        drawer = self.ids.drawer
        overlay = self.ids.overlay

        anim_drawer = Animation(
            x=-drawer.width,
            d=.25,
            t="out_cubic"
        )

        anim_overlay = Animation(
            opacity=0,
            d=.25
        )

        anim_drawer.start(drawer)
        anim_overlay.start(overlay)


        def finalizar(*args):
            overlay.disabled = True
            overlay.size_hint = (None, None)
            overlay.size = (0, 0)

            # impede o drawer invisível de bloquear os botões
            drawer.disabled = True

        anim_overlay.bind(
            on_complete=finalizar
        )
        self.menu_aberto = False


    # BOTÕES
    def abrir_chat(self):
        print("Abrir Chat")


    def abrir_bags(self):
        self.manager.current = "find_bags"

    
    def abrir_perfil(self):
        self.fechar_menu()
        self.manager.current = "profile"