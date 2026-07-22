# app/screens/find_bags.py

from kivy.uix.screenmanager import Screen
from services.bag_service import BagService

class FindBagsScreen(Screen):

    def buscar_bagagem(self):
        # Captura os dados dos campos de texto da tela
        cpf = self.ids.cpf_input.text
        codigo = self.ids.codigo_input.text

        # Consulta a camada de serviço
        bagagem = BagService.buscar_bagagem_demonstracao(cpf, codigo)

        if bagagem:
            # Oculta mensagem de erro se houver
            self.ids.lbl_mensagem_erro.text = ""
            
            # Preenche o card com os dados retornados
            self.ids.lbl_status.text = f"🟢 Status: {bagagem['status']}"
            self.ids.lbl_codigo.text = f"Código: {bagagem['codigo']}"
            self.ids.lbl_passageiro.text = f"Passageiro: {bagagem['passageiro']}"
            self.ids.lbl_cpf.text = f"CPF: {bagagem['cpf']}"
            self.ids.lbl_companhia.text = f"Companhia: {bagagem['companhia']}"
            self.ids.lbl_rota.text = f"Rota: {bagagem['origem']} ➔ {bagagem['destino']}"
            self.ids.lbl_despacho.text = f"Despacho: {bagagem['data_despacho']} às {bagagem['horario_despacho']}"
            self.ids.lbl_localizacao.text = f"Localização: {bagagem['localizacao']}"
            self.ids.lbl_atualizacao.text = f"Última atualização: {bagagem['ultima_atualizacao']}"
            self.ids.lbl_previsao.text = f"Previsão na esteira: {bagagem['previsao_esteira']}"
            
            # Exibe o card de resultado
            self.ids.card_resultado.opacity = 1
            self.ids.card_resultado.disabled = False
        else:
            # Oculta o card e exibe a mensagem de erro amigável
            self.ids.card_resultado.opacity = 0
            self.ids.card_resultado.disabled = True
            self.ids.lbl_mensagem_erro.text = "Bagagem não encontrada. Verifique o CPF e o código informado."