from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    tmdb_id = Column(Integer, unique=True)
    title = Column(String)
    year = Column(String)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    lent_to_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    lent_since = Column(Date, nullable=True)
    poster_url = Column(String)
