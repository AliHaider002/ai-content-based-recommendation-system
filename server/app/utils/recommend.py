import pickle
from app.utils.fetch_movies import fetch_single_movie

with open("app/gen/movies_similarity.pkl", "rb") as f:
    similarity = pickle.load(f)
    
def recommend(df, movie):
    movie_index = df[df["title"] == movie.lower()].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    
    data = []
    
    for i in movie_list:
        movie = fetch_single_movie(int(df.iloc[i[0]].movie_id))
        data.append(movie)
    # print(data)
    return data