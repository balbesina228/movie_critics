from pydantic import BaseModel


class CriticsBase(BaseModel):
    title: str
    text: str | None = None


class CriticsCreate(CriticsBase):
    pass


class Critics(CriticsBase):
    id: int
    owner_id: int
    movie_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    critics: list[Critics] = []

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    description: str | None = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
