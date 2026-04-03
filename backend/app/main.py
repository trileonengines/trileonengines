from fastapi import FastAPI
from .routes.engine import router

app = FastAPI()

@app.get("/")
def root():
    return {"Trileon": "alive"}

app.include_router(router, prefix="/engine")
