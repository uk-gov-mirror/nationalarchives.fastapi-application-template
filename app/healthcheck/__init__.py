from fastapi import APIRouter

router = APIRouter()

from app.healthcheck import routes
