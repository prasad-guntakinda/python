from fastapi import FastAPI
from app.database import Base, engine
from app.routes import book_routes
from app.core.config import APP_NAME

app = FastAPI(title=APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(book_routes.router)
