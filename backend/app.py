from datetime import datetime
from backend.src.application import api
from backend.src.rotas import rota_raiz
from backend.src.rotas.indicadores import rota_ind
from backend.src.rotas.variaveis import rota_var
from fastapi.staticfiles import StaticFiles


@api.on_event('startup')
def __startup():
    """
    Inicialização da API
    """
    print(f'[SC-RIDE] [{datetime.now()}] Iniciando - API')


@api.on_event('shutdown')
def __shutdown():
    """
    O que fazer quando a API é encerrada
    """
    print(f'[SC-RIDE] [{datetime.now()}] Encerrando - API')


api.include_router(rota_raiz)
api.include_router(rota_ind)
api.include_router(rota_var)
api.mount("/static", StaticFiles(
        directory="backend/src/static"), name="static")
