from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers.movie import movies_routes

load_dotenv()
app = FastAPI()

origins = [
    "http://localhost:3000",  # Frontend on localhost
    "http://localhost:5173",  # Frontend on localhost
    "https://your-frontend-domain.com",  # Another domain if necessary
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,  # Allow cookies and credentials
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include routers for different modules
app.include_router(movies_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Movies Recommender System!"}
