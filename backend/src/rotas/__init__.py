import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

rotas = APIRouter()
templates_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
templates = Jinja2Templates(directory=templates_path)


@rotas.get(path="/",
           responses={200: {"description": "Ok", "content": {"image/jpeg": {"example": "pagina"}}},
                      400: {"description": "not found"}},
           tags=["Home"],
           name="Página inicial",
           description="Apresenta página inicial do projeto")
async def home(request: Request):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    return templates.TemplateResponse("index.html", {"request": request})