from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import (
    MDFlatButton,
    MDRaisedButton
)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast

from kivy.properties import (
    StringProperty,
    BooleanProperty
)

from services.user_service import UserService
from core.session import Session


class ProfileScreen(MDScreen):

    usuario = StringProperty("")
    email = StringProperty("")
    cpf = StringProperty("")

    foto = StringProperty(
        "assets/images/avatar_default.png"
    )

    conectado = BooleanProperty(False)

    dialog = None

    service = UserService()

    def on_enter(self):
        user = Session.obter_usuario()

        if not user:
            return

        self.usuario = user.usuario
        self.email = user.email
        self.cpf = user.cpf if user.cpf else ""

        self.verificar_passageiro()


    def verificar_passageiro(self):
        """
        Consulta no banco se existe passageiro
        vinculado ao usuário.
        """
        pass


    def conectar_passageiro(self):
        """
        Abre popup para Nome Completo + CPF
        """
        pass


    def desconectar_passageiro(self):
        """
        Confirma desconexão
        """
        pass


    def editar_perfil(self):
        self.campo_usuario = MDTextField(
            hint_text="Usuário",
            text=self.usuario
        )

        self.campo_email = MDTextField(
            hint_text="Email",
            text=self.email
        )

        self.campo_cpf = MDTextField(
            hint_text="CPF (Opcional)",
            text=self.cpf
        )

        conteudo = MDBoxLayout(
            orientation="vertical",
            spacing="15dp",
            adaptive_height=True
        )

        conteudo.add_widget(self.campo_usuario)
        conteudo.add_widget(self.campo_email)
        conteudo.add_widget(self.campo_cpf)

        self.dialog = MDDialog(
            title="Editar Perfil",
            type="custom",
            content_cls=conteudo,
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="Salvar",
                    on_release=self.salvar_edicao
                )
            ]
        )

        self.dialog.open()


    def salvar_edicao(self, *args):
        usuario = self.campo_usuario.text.strip()
        email = self.campo_email.text.strip()
        cpf = self.campo_cpf.text.strip()

        if not usuario or not email:
            toast("Usuário e email são obrigatórios.")
            return

        usuario_logado = Session.obter_usuario()

        sucesso, resultado = self.service.editar_usuario(
            usuario_logado.id,
            usuario,
            email,
            cpf
        )

        if not sucesso:

            if resultado == "usuario":
                toast("Este usuário já está em uso.")
                return

            if resultado == "email":
                toast("Este email já está em uso.")
                return

            if resultado == "cpf":
                toast("Este CPF já está em uso.")
                return

            toast("Erro ao atualizar usuário.")
            return

        # Atualiza a sessão
        Session.salvar_usuario(resultado)

        # Atualiza esta tela
        self.on_enter()

        # Atualiza Home
        home = self.manager.get_screen("home")
        home.on_enter()

        # Atualiza Drawer
        home.ids.drawer.carregar_usuario()

        self.dialog.dismiss()

        toast("Perfil atualizado com sucesso!")


    def voltar(self):
        self.manager.current = "home"