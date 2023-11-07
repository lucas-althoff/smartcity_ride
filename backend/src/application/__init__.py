from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

api = FastAPI(version='0.0.1', docs_url='/docs', redoc_url='/redoc', title="Smart City - RIDE")

origins = [
    "https://smartcity-survey.vercel.app/",
    "http://localhost:3000"
]

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_origins=origins
)
