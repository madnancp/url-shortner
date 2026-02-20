from fastapi import FastAPI
from src.config import settings
from src.database import Base, engine

Base.metadata.create_all(engine)
app = FastAPI(
    title="Url Shortener",
    version="0.1.0",
    debug=settings.DEBUG,
)
