from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import User
from passlib.hash import bcrypt
import os

router = APIRouter()

@router.on_event("startup")
def create_admin():
    db = SessionLocal()
    if not db.query(User).filter(User.username == os.getenv("ADMIN_USERNAME")).first():
        admin = User(
            username=os.getenv("ADMIN_USERNAME"),
            password_hash=bcrypt.hash(os.getenv("ADMIN_PASSWORD")),
            email="admin@example.com"
        )
        db.add(admin)
        db.commit()

@router.post("/")
def create_user(username: str, password: str, email: str = None):
    db = SessionLocal()
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(username=username, email=email, password_hash=bcrypt.hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/")
def list_users():
    db = SessionLocal()
    return db.query(User).all()
