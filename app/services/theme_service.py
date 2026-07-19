from kivy.storage.jsonstore import JsonStore
import os


class ThemeService:

    """
    Responsável por salvar e recuperar localmente a preferência
    de tema (Claro/Escuro) do usuário, usando o JsonStore do Kivy.
    """

    NOME_ARQUIVO = "theme_store.json"
    CHAVE = "preferencias"


    def __init__(self):

        caminho_app = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.store = JsonStore(
            os.path.join(caminho_app, self.NOME_ARQUIVO)
        )


    def carregar_tema(self, padrao="Light"):

        try:

            if self.store.exists(self.CHAVE):
                return self.store.get(self.CHAVE).get("theme_style", padrao)

        except Exception:
            pass

        return padrao


    def salvar_tema(self, theme_style):

        try:

            self.store.put(
                self.CHAVE,
                theme_style=theme_style
            )

        except Exception:
            pass