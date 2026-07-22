class BagService:
    @staticmethod
    def buscar_bagagem_demonstracao(cpf: str, codigo: str) -> dict | None:
        """
        Método temporário de demonstração para busca de bagagem.
        Retorna os dados da bagagem se CPF e código coincidirem com o mock.
        """
        # Normalização simples de espaços
        cpf_limpo = cpf.strip() if cpf else ""
        codigo_limpo = codigo.strip().upper() if codigo else ""

        # Dado estático fictício para a apresentação
        MOCK_BAGAGEM = {
            "status": "Em transporte",
            "codigo": "BAG-2026-001",
            "passageiro": "Felipe Vieira",
            "cpf": "123.456.789-00",
            "companhia": "BagConnect Airlines",
            "origem": "Rio de Janeiro (GIG)",
            "destino": "São Paulo (GRU)",
            "data_despacho": "22/07/2026",
            "horario_despacho": "09:35",
            "localizacao": "Centro de Distribuição - São Paulo",
            "ultima_atualizacao": "Hoje às 10:42",
            "previsao_esteira": "15 minutos"
        }

        # Validação estrita
        if cpf_limpo == MOCK_BAGAGEM["cpf"] and codigo_limpo == MOCK_BAGAGEM["codigo"]:
            return MOCK_BAGAGEM
        
        return None