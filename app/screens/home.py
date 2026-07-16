from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.animation import Animation


class HomeScreen(MDScreen):

    nome_usuario = StringProperty("Usuário")

    menu_aberto = False

    # MENU

    def abrir_menu(self):

        if self.menu_aberto:
            return

        drawer = self.ids.drawer
        overlay = self.ids.overlay

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

        anim_overlay.bind(on_complete=finalizar)

        self.menu_aberto = False

    # BOTÕES

    def abrir_chat(self):
        print("Abrir Chat")

    def abrir_bags(self):
        print("Abrir Bagagens")