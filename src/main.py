from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controller.http.router import api_router

application = FastAPI()
application.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
application.include_router(api_router)
