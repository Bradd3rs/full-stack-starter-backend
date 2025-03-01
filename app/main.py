from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.settings import settings
from app.db.session import engine, Base

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="full-stack-starter-backend",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to full-stack-starter-backend API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"} 