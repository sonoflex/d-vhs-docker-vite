from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import movies

app = FastAPI(title="D-VHS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movies.router, prefix="/movies", tags=["movies"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])