from sqlalchemy.orm import Session

from src import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """
    The password has to be hashed! EDIT ME!
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_movies(db: Session, skip: int = 0, limit: int = 15):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def create_movie(db: Session, movie: schemas.MovieCreate, movie_id: int):
    db_movie = models.Movie(**movie.model_dump(), id=movie_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movie_critics(db: Session, movie_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Critics).filter(models.Movie.movie_critics == movie_id).offset(skip).limit(limit).all()


def get_user_critics(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Critics).filter(models.User.critics == user_id).offset(skip).limit(limit).all()


def create_movie_critics(db: Session, critics: schemas.CriticsCreate, user_id: int, movie_id: int):
    db_critics = models.Critics(**critics.model_dump(), owner_id=user_id, movie_id=movie_id)
    db.add(db_critics)
    db.commit()
    db.refresh(db_critics)
    return db_critics
