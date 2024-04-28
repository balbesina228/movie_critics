from fastapi import FastAPI, HTTPException

from database import SessionLocal
from models import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the home page!"}


@app.get("/movies")
async def movies():
    return {"message": "Here's gonna be all the movies"}


@app.get("/movies/{movie_id}")
async def read_movie(movie_id: int):
    return {"movie_id": movie_id, "message": "Here's gonna be all the information about one single movie"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
