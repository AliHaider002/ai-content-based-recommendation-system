from pydantic import BaseModel

class Movies(BaseModel):
    title: str
    
class Movie(BaseModel):
    id: int
