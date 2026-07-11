from app.api.auth import router as auth_router
from fastapi import FastAPI
from app.database.database import Base, engine

# Import models so SQLAlchemy knows about them
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Financial Intelligence Platform",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Financial Intelligence Platform "
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }