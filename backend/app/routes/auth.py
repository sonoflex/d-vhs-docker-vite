from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import User
from passlib.hash import bcrypt
import os

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user or not bcrypt.verify(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}
