from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True)

    critics = relationship("Critics", back_populates="owner")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String)

    movie_critics = relationship("Critics", back_populates="movie")


class Critics(Base):
    __tablename__ = "critics"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))

    owner = relationship("User", back_populates="critics")
    movie = relationship("Movie", back_populates="movie_critics")
