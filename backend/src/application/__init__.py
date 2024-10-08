from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

api = FastAPI(version='0.0.1', docs_url='/docs', redoc_url='/redoc', title="API e-RIDE")

origins = [
    "https://smartcity-survey.vercel.app/",
    "https://smartcity-survey-git-main-lucas-althoffs-projects.vercel.app/",
    "https://smartcity-survey-fack79bkj-lucas-althoffs-projects.vercel.app/",
    "https://smartcity-survey-ioijizhvr-lucas-althoffs-projects.vercel.app/",
    "http://localhost:3000"
]

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_origins=['*']
)


@api.options("/survey/complete",
             include_in_schema=False)
async def survey_complete_options():
    # Handle preflight requests
    return {"message": "Preflight request allowed"}