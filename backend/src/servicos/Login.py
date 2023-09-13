import os
import base64


class Login:
    """
    Classe contendo os atributos e métodos para realizar Login na API CERC
    """

    def __init__(self) -> None:
        """Iniciar atributos de para gerar token de login
        :return: inicializacao das credenciais a partir das variaveis ambientes
        :rtype: <NoneType>
        """
        self.username = os.environ["username"]
        self.senha = os.environ["senha"]
        self.oauthclientid = os.environ["clientid"]
        self.oauthclientsecret = os.environ["clientsecret"]
        self.url_token = ""

    def gerar_basic_auth_header(self) -> dict:
        """Gerar um header para Basic authentication a partir de senha e username
        :return: Auth header contendo um Basic authentication com o token criptografado
        :rtype: <dict>
        """
        credentials = f"{self.username}:{self.senha}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
            "utf-8"
        )
        basic_auth_token = f"Basic {encoded_credentials}"
        return {"Authorization": basic_auth_token}

    def gerar_credentials_oauth(self) -> dict:
        """Gerar payload para Oauth authentication a partir de ClientID e ClientSecret
        :return: Payload em formato multipart JSON contendo credenciais oauth
        :rtype: <dict>
        """
        return {
            "grant_type": "client_credentials",
            "username": self.oauthclientid,
            "password": self.oauthclientsecret,
        }

    async def gerar_token(self) -> str:
        """Requisitar token usando Oauth authentication
        :return: Token gerado pelo servidor de autenticacao da CERC
            :Em caso de sucesso: string contendo token
                :Exemplo: 'e7807fa7-3c76-451b-8934-da2d71f25d3c'
            :Em caso de erro: HTTPException(401)
        :rtype: <string>
        """
        self.auth_header = self.gerar_basic_auth_header()
        self.auth_body = self.gerar_credentials_oauth()
