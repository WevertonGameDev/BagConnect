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

import re

from core.session import Session
from services.user_service import UserService


class ProfileScreen(MDScreen):

    usuario = StringProperty("")
    email = StringProperty("")
    cpf = StringProperty("")

    foto = StringProperty(
        "assets/images/avatar_default.png"
    )

    conectado = BooleanProperty(False)

    dialog = None
    botao_salvar = None


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

        self.campo_usuario.bind(
            text=self.verificar_alteracoes
        )

        self.campo_email.bind(
            text=self.verificar_alteracoes
        )

        self.campo_cpf.bind(
            text=self.verificar_alteracoes
        )

        conteudo = MDBoxLayout(
            orientation="vertical",
            spacing="15dp",
            adaptive_height=True
        )

        conteudo.add_widget(self.campo_usuario)
        conteudo.add_widget(self.campo_email)
        conteudo.add_widget(self.campo_cpf)

        self.botao_salvar = MDRaisedButton(
            text="Salvar",
            disabled=True,
            on_release=self.salvar_edicao
        )

        self.dialog = MDDialog(
            title="Editar Perfil",
            type="custom",
            content_cls=conteudo,
            buttons=[
                MDFlatButton(
                    text="Cancelar",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                self.botao_salvar
            ]
        )

        self.dialog.open()
        self.verificar_alteracoes()


    def verificar_alteracoes(self, *args):

        # Validação visual do Email 
        if self.validar_email(self.campo_email.text.strip()):
            self.campo_email.error = False

        else:
            self.campo_email.error = True

        # Validação visual do CPF 
        cpf = (
            self.campo_cpf.text
            .replace(".", "")
            .replace("-", "")
            .strip()
        )

        if cpf == "" or self.validar_cpf(cpf):
            self.campo_cpf.error = False

        else:
            self.campo_cpf.error = True


        # Verifica alterações 
        alterado = (
            self.campo_usuario.text.strip() != self.usuario or
            self.campo_email.text.strip() != self.email or
            self.campo_cpf.text.strip() != self.cpf
        )

        valido = (
            self.campo_usuario.text.strip() != "" and
            not self.campo_email.error and
            not self.campo_cpf.error
        )


        self.botao_salvar.disabled = not (alterado and valido)


    def validar_email(self, email):

        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        return re.match(
            padrao,
            email
        ) is not None


    def validar_cpf(self, cpf):
        cpf = cpf.replace(".", "").replace("-", "")

        if cpf == "":
            return True

        return cpf.isdigit() and len(cpf) == 11


    def salvar_edicao(self, *args):
        usuario = self.campo_usuario.text.strip()
        email = self.campo_email.text.strip()
        cpf = self.campo_cpf.text.strip()

        if usuario == "":
            toast("Informe um usuário.")
            return

        if not self.validar_email(email):
            toast("Email inválido.")
            return

        if not self.validar_cpf(cpf):
            toast("CPF inválido.")
            return

        service = UserService()

        sucesso, retorno = service.editar_usuario(
            Session.obter_usuario().id,
            usuario,
            email,
            cpf
        )

        if sucesso:

            Session.salvar_usuario(retorno)

            self.usuario = retorno.usuario
            self.email = retorno.email
            self.cpf = retorno.cpf if retorno.cpf else ""

            toast("Perfil atualizado.")

            self.dialog.dismiss()

        else:

            if retorno == "usuario":
                toast("Este usuário já existe.")

            elif retorno == "email":
                toast("Este email já está em uso.")

            elif retorno == "cpf":
                toast("Este CPF já está cadastrado.")

            else:
                toast("Erro ao atualizar perfil.")


    def voltar(self):
        self.manager.current = "home"