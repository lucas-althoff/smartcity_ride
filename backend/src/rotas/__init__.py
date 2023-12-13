import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


rota_raiz = APIRouter()
templates_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'templates')
templates = Jinja2Templates(directory=templates_path)


def criar_saida(content, message=''):
    return {"message": message,
            "content": content}


@rota_raiz.get(path="/",
               responses={200: {"description": "Ok",
                                "content": {"image/jpeg": {"example": "pagina"}}},
                          400: {"description": "not found"}},
               tags=["Home"],
               name="Página inicial",
               description="Apresenta página inicial do projeto", include_in_schema=False)
async def home(request: Request):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    return templates.TemplateResponse("index.html", {"request": request})

@rota_raiz.get("/healthcheck", include_in_schema=False)
def read_root():
    return {"status": "ok"}