# app/routes/movies.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_movies():
    return [{"title": "Star Wars"}, {"title": "The Matrix"}, {"title": "Inception"}]
