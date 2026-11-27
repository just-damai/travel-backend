from fastapi import FastAPI

from app.api.translate import router as translate_router

app = FastAPI(title="Travel Translator API", version="1.0.0")

app.include_router(translate_router, prefix="/api/v1")