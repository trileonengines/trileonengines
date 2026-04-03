from fastapi import APIRouter
from app.core.engine import run_engine

router = APIRouter()

@router.post("/run")
def run(payload: dict):
    return run_engine(payload)