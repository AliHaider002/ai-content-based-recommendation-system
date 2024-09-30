import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer

class Wrangle:
    def __init__(self):
        pass
    
    def convert_txt_string(self, obj):
        data = []
        for i in ast.literal_eval(obj):
            data.append(i["name"])
        return data
    
    def getCast(self, obj):
        data = []
        counter = 0
        for i in ast.literal_eval(obj):
            if counter != 3:
                data.append(i["name"])
                counter += 1
            else:
                break
        return data
    
    def stem(self, text):
        ps = PorterStemmer()
        y = []
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)
    
    def getDirector(self, obj):
        data = []
        for i in ast.literal_eval(obj):
            if i["job"] == "Director":
                data.append(i["name"])
        return data
    
    def process(self, set1, set2):
        credits = pd.read_csv(set1)
        movies = pd.read_csv(set2)
        df = movies.merge(credits, left_on="title",right_on="title")
        df.drop(columns=["id", "budget", "homepage", "original_language", "original_title","popularity", "production_companies", "production_countries", "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline", "vote_average", "vote_count"], inplace=True)

        df.dropna(inplace=True)
        
        df["genres"] = df["genres"].apply(self.convert_txt_string)
        df["genres"] = df["genres"].apply(lambda x: [i.replace(" ", "_")  for i in x ])
        
        df["keywords"] = df["keywords"].apply(self.convert_txt_string)
        df["keywords"] = df["keywords"].apply(lambda x: [i.replace(" ", "_")  for i in x ])
        
        df["cast"] = df["cast"].apply(self.getCast)
        df["cast"] = df["cast"].apply(lambda x: [i.replace(" ", "_")  for i in x ])
        
        df["crew"] = df["crew"].apply(self.getDirector)
        df["crew"] = df["crew"].apply(lambda x: [i.replace(" ", "_")  for i in x ])
        
        df["overview"] = df["overview"].apply(lambda x: x.split())

        df["tags"] = df["overview"] + df["genres"] + df["keywords"] + df["cast"] + df["crew"]

        new_df = df[["movie_id", "title", "tags"]]

        new_df["title"] = new_df["title"].apply(lambda x: x.lower()) 
        new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x)) 
        new_df["tags"] = new_df["tags"].apply(self.stem) 
        
        new_df.to_csv("app/gen/data.csv")

        return new_df
    