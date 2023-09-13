# Smart City RIDE
Solução de ETL para execução da Ação 1 da Expo Ride, voltado para calcular o diagnóstico de maturidade de cidades inteligentes.

## Backend

## Preparando ambiente

`conda create -n sc-ride python=3.11 pip git fastapi uvicorn pandas jinja2`

`pip install supabase`

`pip install fastapi`

`pip install decouple`

`uvicorn backend.app:api --port 7777 --reload` 