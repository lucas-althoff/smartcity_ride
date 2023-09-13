from fastapi import HTTPException
from Login import Login


async def executar_login() -> str:
    """Função que encapsula o Login, realizando o login na API CERC e recebendo o token de acesso
    :entrada: <string> contendo dicionário cifrado com as chaves "username", "password" e "numeroTipoServico"
    :retorno: username, password
        :Em caso de erro: curio_erros_excecoes(500)
    :rtype: <string>
    """
    auth = Login()
    try:
        bearer = await auth.gerar_credentials_oauth()
    except Exception:
        raise HTTPException(status_code=500, detail="Erro")
    del auth
    return bearer