from backend.application import api
from backend.rotas import rotas
from fastapi.staticfiles import StaticFiles


@api.on_event('startup')
def __startup():
    """
    Inicialização da API
    """
    print(f'Iniciando - API')


@api.on_event('shutdown')
def __shutdown():
    """
    O que fazer quando a API é encerrada
    """
    print(f'Encerrando - API')


api.include_router(rotas)
api.mount("/static", StaticFiles(
        directory="backend/static"), name="static")
