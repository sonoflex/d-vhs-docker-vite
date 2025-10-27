from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import Movie
from app.tmdb import get_movie_details
from datetime import date

router = APIRouter()

@router.get("/")
def list_movies():
    db = SessionLocal()
    return db.query(Movie).all()

@router.post("/")
def add_movie(tmdb_id: int, owner_id: int):
    db = SessionLocal()
    if db.query(Movie).filter(Movie.tmdb_id == tmdb_id).first():
        raise HTTPException(status_code=400, detail="Film bereits vorhanden")
    data = get_movie_details(tmdb_id)
    movie = Movie(
        tmdb_id=tmdb_id,
        title=data["title"],
        year=data["year"],
        description=data["description"],
        poster_url=data["poster_url"],
        owner_id=owner_id
    )
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie
