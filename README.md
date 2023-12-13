# API e-RIDE
Solução de ETL para execução da Ação 1 da Expo Ride, voltado para calcular o diagnóstico de maturidade de cidades inteligentes.

## Backend

## Preparando ambiente local

`conda create -n sc-ride python=3.11 pip git fastapi uvicorn pandas jinja2`

`pip install supabase`

`pip install fastapi`

`pip install decouple`

`uvicorn backend.app:api --port 7777 --reload` 

## Configurar APP no fly io

- Checar configuração da máquina no arquivo fly.toml

## Deploy no fly io

```shell
fly secrets set SUPABASE_KEY_PUB=<KEY>
fly launch
```