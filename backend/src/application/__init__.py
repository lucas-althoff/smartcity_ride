from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

api = FastAPI(version='0.0.1', docs_url='/docs', redoc_url='/redoc', title="Smart City - RIDE")

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["http://localhost:3000"]
)
