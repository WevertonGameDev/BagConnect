class Session:

    usuario_atual = None

    @classmethod
    def salvar_usuario(cls, usuario):
        cls.usuario_atual = usuario

    @classmethod
    def obter_usuario(cls):
        return cls.usuario_atual

    @classmethod
    def logout(cls):
        cls.usuario_atual = None