from pydantic import BaseModel
from typing import Optional

class MovieBase(BaseModel):
    tmdb_id: int
    title: str
    year: str
    description: str
    poster_url: Optional[str] = None
    owner_id: Optional[int] = None

class MovieCreate(BaseModel):
    tmdb_id: int
    owner_id: int

class Movie(MovieBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
