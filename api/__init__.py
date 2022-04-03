from fastapi import APIRouter
from api import (
    system,
    lists
)


router = APIRouter()


router.include_router(system.router)
router.include_router(lists.router, prefix="/api")
