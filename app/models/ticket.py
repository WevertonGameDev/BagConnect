class Ticket:

    lista = []

    contador = 1

    def __init__(
        self,
        assunto,
        descricao,
        cpf,
        codigo_bag,
    ):

        self.id = Ticket.contador
        Ticket.contador += 1

        self.assunto = assunto
        self.descricao = descricao
        self.cpf = cpf
        self.codigo_bag = codigo_bag

        self.status = "Aguardando Atendimento"

        self.mensagens = []

    def adicionar_mensagem(
        self,
        autor,
        texto,
    ):

        self.mensagens.append(
            {
                "autor": autor,
                "texto": texto,
            }
        )

    def salvar(self):

        Ticket.lista.append(self)