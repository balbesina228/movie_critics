from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Welcome to the home page!"}


@app.get("/movies", response_model=list[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(
        db=db, movie_id=movie_id, movie=movie
    )


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}/critics/", response_model=list[schemas.Critics])
def read_user_critics(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_critics(db=db, user_id=user_id)


@app.get("/movies/{movie_id}/critics/", response_model=list[schemas.Critics])
def read_movie_critics(movie_id: int, db: Session = Depends(get_db)):
    return crud.get_movie_critics(db=db, movie_id=movie_id)


@app.post("/movies/{movie_id}/critics", response_model=schemas.Critics)
def create_movie_critics(
        movie_id: int, critics: schemas.CriticsCreate,
        owner_id: int, db: Session = Depends(get_db)
):
    return crud.create_movie_critics(
        db=db, critics=critics, movie_id=movie_id, user_id=owner_id
    )
