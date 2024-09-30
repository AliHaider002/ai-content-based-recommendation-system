import os
from fastapi import APIRouter
from app.models.movies import Movies, Movie
from app.routers.movie.movies_dao import get_movie, get_title_dict, generate_data_csv, get_recommendations

router = APIRouter()

@router.get("/get/{id}")
async def get_movies(id: int):
    
    data = get_movie(id)
    return data

@router.get("/titles")
async def read_items():
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'gen', 'data.csv')
    titles = get_title_dict(path)
    return list(titles.values())


@router.get("/generate")
async def generate_csv():
    path1 = os.path.join(os.path.dirname(__file__), '..', '..', 'gen', 'tmdb_5000_credits.csv')
    path2 = os.path.join(os.path.dirname(__file__), '..', '..', 'gen', 'tmdb_5000_movies.csv')
    titles = generate_data_csv(file_path1=path1, file_path2=path2)
    return {"status" : 200, "message": "The Movies name csv generated Successfully"}

@router.post("/recommend")
async def get_recommendation(movie: Movies):
    path = os.path.join(os.path.dirname(__file__), '..', '..', 'gen', 'data.csv')
    resp = await get_recommendations(file_path=path, movie_name=movie.title)
    return {"status" : 200, "data": resp}