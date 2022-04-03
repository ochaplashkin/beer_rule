from fastapi import APIRouter

router = APIRouter(prefix="", tags=["systsem"])


@router.get("/health")
async def health():
    return {"status": "ok"}
