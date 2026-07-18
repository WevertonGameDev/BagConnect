from locale import getdefaultlocale


class Tradutor:
    #Centraliza os textos do app em português e inglês.

    def __init__(self):
        self.idioma = self._detectar_idioma()
        self.textos = {
            "pt": {
                "app_nome": "BagConnect",
                "login_subtitulo": "Conectando você ao suporte",
                "login_titulo": "Entrar",
                "login_botao": "ENTRAR",
                "criar_conta": "Criar uma conta",
                "rodape_app": "© BagConnect",
                "campo_email": "Email",
                "campo_senha": "Senha",
                "perfil_cpf_opcional": "CPF (Opcional)",
                "perfil_editar_titulo": "Editar Perfil",
                "perfil_salvar": "Salvar",
                "perfil_cancelar": "Cancelar",
                "perfil_informe_usuario": "Informe um usuário.",
                "perfil_email_invalido": "Email inválido.",
                "perfil_cpf_invalido": "CPF inválido.",
                "perfil_atualizado": "Perfil atualizado.",
                "perfil_usuario_ja_existe": "Este usuário já existe.",
                "perfil_email_ja_uso": "Este email já está em uso.",
                "perfil_cpf_ja_cadastrado": "Este CPF já está cadastrado.",
                "perfil_erro_atualizar": "Erro ao atualizar perfil.",
                "cadastro_titulo": "Criar conta",
                "cadastro_subtitulo": "Cadastre-se no BagConnect",
                "campo_usuario": "Usuário",
                "campo_confirmar_senha": "Confirmar senha",
                "cadastro_botao": "CADASTRAR",
                "ja_tenho_conta": "Já tenho uma conta",
                "home_ola": "Olá",
                "home_bem_vindo": "Bem-vindo ao BagConnect",
                "home_suporte": "Suporte",
                "home_suporte_texto": "Converse com nossa equipe de atendimento",
                "home_bags": "Minhas Bagagens",
                "home_bags_texto": "Consulte informações das suas bags",
                "home_botao_chat": "ABRIR CHAT",
                "home_botao_bags": "CONSULTAR",
                "home_bagagens_titulo": "Minhas Bagagens",
                "home_bagagens_texto": "Consulte o status das suas bagagens em tempo real.",
                "home_botao_bagagem": "Encontrar Bagagem",
                "home_suporte_titulo": "Suporte",
                "home_suporte_texto": "Converse com nossa equipe através do chat.",
                "home_botao_suporte": "Abrir Chat",
                "home_usuario_padrao": "Usuário",
                "home_email_padrao": "usuario@gmail.com",
                "find_bags_titulo": "Minhas Bagagens",
                "find_bags_cpf": "CPF",
                "find_bags_cpf_hint": "Digite seu CPF",
                "find_bags_cpf_helper": "Somente o proprietário da bagagem pode consultá-la.",
                "find_bags_codigo": "Código da Bagagem",
                "find_bags_codigo_hint": "Ex.: BAG000123",
                "find_bags_codigo_helper": "Código informado no despacho.",
                "find_bags_botao_consultar": "Consultar Bagagem",
                "find_bags_encontrada": "Bag encontrada",
                "find_bags_status": "Status",
                "find_bags_atencao": "Atenção",
                "find_bags_preencha_campos": "Preencha o CPF e o código da bagagem.",
                "find_bags_nao_encontrada": "Bagagem não encontrada",
                "find_bags_nao_encontrada_texto": "Não foi encontrada nenhuma bagagem para os dados informados.",
                "find_bags_status_prefix": "Status:",
                "find_bags_resultado_sucesso": "Bagagem localizada com sucesso.",
                "find_bags_ok": "OK",
                "menu_home": "Início",
                "menu_bagagens": "Bagagens",
                "menu_suporte": "Suporte",
                "menu_perfil": "Perfil",
                "menu_configuracoes": "Configurações",
                "menu_sair": "Sair",
                "perfil_titulo": "Perfil",
                "perfil_conectado": "Conectado como Passageiro",
                "perfil_nao_conectado": "Não conectado",
                "perfil_desconectar": "Desconectar",
                "perfil_conectar": "Conectar",
                "toast_login_realizado": "Login realizado",
                "toast_login_erro": "Informe email e senha",
                "toast_preencha_campos": "Preencha todos os campos",
                "toast_senhas_nao_conferem": "As senhas não conferem",
                "toast_cadastro_realizado": "Cadastro realizado",
                "toast_erro_cadastrar": "Erro ao cadastrar",
                "toast_email_invalido": "Email inválido",
                "toast_senha_curta": "A senha deve possuir no mínimo 6 caracteres",
                "tema_escuro": "Tema escuro"
            },
            "en": {
                "app_nome": "BagConnect",
                "login_subtitulo": "Connecting you to support",
                "login_titulo": "Sign in",
                "login_botao": "SIGN IN",
                "criar_conta": "Create an account",
                "rodape_app": "© BagConnect",
                "campo_email": "Email",
                "campo_senha": "Password",
                "perfil_cpf_opcional": "CPF (Optional)",
                "perfil_editar_titulo": "Edit Profile",
                "perfil_salvar": "Save",
                "perfil_cancelar": "Cancel",
                "perfil_informe_usuario": "Please enter a username.",
                "perfil_email_invalido": "Invalid email.",
                "perfil_cpf_invalido": "Invalid CPF.",
                "perfil_atualizado": "Profile updated.",
                "perfil_usuario_ja_existe": "This username already exists.",
                "perfil_email_ja_uso": "This email is already in use.",
                "perfil_cpf_ja_cadastrado": "This CPF is already registered.",
                "perfil_erro_atualizar": "Error updating profile.",
                "cadastro_titulo": "Create account",
                "cadastro_subtitulo": "Register on BagConnect",
                "campo_usuario": "User",
                "campo_confirmar_senha": "Confirm password",
                "cadastro_botao": "REGISTER",
                "ja_tenho_conta": "I already have an account",
                "home_ola": "Hello",
                "home_bem_vindo": "Welcome to BagConnect",
                "home_suporte": "Support",
                "home_suporte_texto": "Talk to our support team",
                "home_bags": "My Bags",
                "home_bags_texto": "Check information about your bags",
                "home_botao_chat": "OPEN CHAT",
                "home_botao_bags": "CHECK",
                "home_bagagens_titulo": "My Bags",
                "home_bagagens_texto": "Check the status of your bags in real time.",
                "home_botao_bagagem": "Find Bag",
                "home_suporte_titulo": "Support",
                "home_suporte_texto": "Talk to our team through chat.",
                "home_botao_suporte": "Open Chat",
                "home_usuario_padrao": "User",
                "home_email_padrao": "user@gmail.com",
                "find_bags_titulo": "My Bags",
                "find_bags_cpf": "CPF",
                "find_bags_cpf_hint": "Enter your CPF",
                "find_bags_cpf_helper": "Only the baggage owner can consult it.",
                "find_bags_codigo": "Baggage Code",
                "find_bags_codigo_hint": "Ex.: BAG000123",
                "find_bags_codigo_helper": "Code provided at check-in.",
                "find_bags_botao_consultar": "Check Baggage",
                "find_bags_encontrada": "Bag found",
                "find_bags_status": "Status",
                "find_bags_atencao": "Attention",
                "find_bags_preencha_campos": "Please fill in the CPF and baggage code.",
                "find_bags_nao_encontrada": "Baggage not found",
                "find_bags_nao_encontrada_texto": "No baggage was found for the provided information.",
                "find_bags_status_prefix": "Status:",
                "find_bags_resultado_sucesso": "Baggage located successfully.",
                "find_bags_ok": "OK",
                "menu_home": "Home",
                "menu_bagagens": "Bags",
                "menu_suporte": "Support",
                "menu_perfil": "Profile",
                "menu_configuracoes": "Settings",
                "menu_sair": "Logout",
                "perfil_titulo": "Profile",
                "perfil_conectado": "Connected as Passenger",
                "perfil_nao_conectado": "Not connected",
                "perfil_desconectar": "Disconnect",
                "perfil_conectar": "Connect",
                "toast_login_realizado": "Login successful",
                "toast_login_erro": "Please enter your email and password",
                "toast_preencha_campos": "Please fill in all fields",
                "toast_senhas_nao_conferem": "Passwords do not match",
                "toast_cadastro_realizado": "Registration successful",
                "toast_erro_cadastrar": "Registration error",
                "toast_email_invalido": "Invalid email",
                "toast_senha_curta": "Password must have at least 6 characters",
                "home_bags": "My Bags"
                "tema_escuro": "Dark theme"
            },
        }

    def _detectar_idioma(self):
        codigo_local = getdefaultlocale()[0] or ""
        if not codigo_local:
            return "en"

        idioma = codigo_local.split("_")[0].split("-")[0].lower()

        if idioma.startswith("pt"):
            return "pt"

        if idioma.startswith("en"):
            return "en"

        return "en"

    def traduzir(self, chave, valor_padrao=None):
        idioma = self.idioma
        texto = self.textos[idioma].get(chave)

        if texto is None and valor_padrao is not None:
            return valor_padrao

        if texto is None:
            return chave

        return texto
