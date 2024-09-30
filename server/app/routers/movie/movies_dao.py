import pandas as pd
from app.utils.wrangle import Wrangle
from app.utils.recommend import recommend
from app.utils.fetch_movies import fetch_movie

wrangle = Wrangle()

def get_movie(id):
    data = fetch_movie(id)
    return data

def generate_data_csv(file_path1: str, file_path2: str) -> dict:
    """
    Function to read a CSV file and return the 'title' column as a dictionary.
    The key will be the index of the row and the value will be the title.
    """
    df = wrangle.process(file_path1, file_path2)
    return df['title'].to_dict()

def get_title_dict(file_path: str) -> dict:
    """
    Function to read a CSV file and return the 'title' column as a dictionary.
    The key will be the index of the row and the value will be the title.
    """
    df = pd.read_csv(file_path)
    return df['title'].to_dict()

async def get_recommendations(file_path: str, movie_name: str):
    df = pd.read_csv(file_path)
    
    movies = recommend(df=df, movie=movie_name)
    return movies