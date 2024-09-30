import os
import requests

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_movie(page_id):
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page_id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjVmY2E3ZDg0YWI5MzU0NDAzYTk1YmY3ZWM2NTViYSIsIm5iZiI6MTcyNjUyMTY1MC43NTE0ODcsInN1YiI6IjY2ZThhMDdlYzI2OTRlMWU1N2ExYWJiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kaIKJPKu5-_IS0n8XtjD6iVrDKprFUGtjDlKmB5f7fA"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def fetch_single_movie(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYjVmY2E3ZDg0YWI5MzU0NDAzYTk1YmY3ZWM2NTViYSIsIm5iZiI6MTcyNjUyMTY1MC43NTE0ODcsInN1YiI6IjY2ZThhMDdlYzI2OTRlMWU1N2ExYWJiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kaIKJPKu5-_IS0n8XtjD6iVrDKprFUGtjDlKmB5f7fA"
    }

    response = requests.get(url, headers=headers)
    
    return response.json()