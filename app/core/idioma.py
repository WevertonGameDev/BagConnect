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
                "cadastro_titulo": "Criar conta",
                "cadastro_subtitulo": "Cadastre-se no BagConnect",
                "campo_nome": "Nome completo",
                "campo_confirmar_senha": "Confirmar senha",
                "cadastro_botao": "CADASTRAR",
                "ja_tenho_conta": "Já tenho uma conta",
                "home_ola": "Olá, Cliente!",
                "home_bem_vindo": "Bem-vindo ao BagConnect",
                "home_suporte": "Suporte",
                "home_suporte_texto": "Converse com nossa equipe de atendimento",
                "home_bags": "Minhas Bags",
                "home_bags_texto": "Consulte informações das suas bags",
                "home_botao_chat": "ABRIR CHAT",
                "home_botao_bags": "CONSULTAR",
                "toast_login_realizado": "Login realizado",
                "toast_login_erro": "Informe email e senha",
                "toast_preencha_campos": "Preencha todos os campos",
                "toast_senhas_nao_conferem": "As senhas não conferem",
                "toast_cadastro_realizado": "Cadastro realizado",
                "toast_erro_cadastrar": "Erro ao cadastrar",
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
                "cadastro_titulo": "Create account",
                "cadastro_subtitulo": "Register on BagConnect",
                "campo_nome": "Full name",
                "campo_confirmar_senha": "Confirm password",
                "cadastro_botao": "REGISTER",
                "ja_tenho_conta": "I already have an account",
                "home_ola": "Hello, Customer!",
                "home_bem_vindo": "Welcome to BagConnect",
                "home_suporte": "Support",
                "home_suporte_texto": "Talk to our support team",
                "home_bags": "My Bags",
                "home_bags_texto": "Check information about your bags",
                "home_botao_chat": "OPEN CHAT",
                "home_botao_bags": "CHECK",
                "toast_login_realizado": "Login successful",
                "toast_login_erro": "Please enter your email and password",
                "toast_preencha_campos": "Please fill in all fields",
                "toast_senhas_nao_conferem": "Passwords do not match",
                "toast_cadastro_realizado": "Registration successful",
                "toast_erro_cadastrar": "Registration error",
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
