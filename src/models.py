from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True)

    critics = relationship("Critics", back_populates="owner")


class Critics(Base):
    __tablename__ = "critics"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    text = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="critics")
