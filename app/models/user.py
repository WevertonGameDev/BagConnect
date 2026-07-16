class User:

    def __init__(
        self,
        id=None,
        usuario=None,
        email=None,
        senha=None,
        cpf=None,
        passageiro_id=None
    ):

        self.id = id
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.passageiro_id = passageiro_id