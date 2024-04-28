from fastapi import FastAPI

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
