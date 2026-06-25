from fastapi import APIRouter, Depends
from backend.app.services.comparison import ComparisonService
from backend.app.core.deps import get_comparison_service

router = APIRouter(prefix="/compare", tags=["compare"])

@router.get("/{user1}/{user2}")
async def compare(
    user1: str,
    user2: str,
    service: ComparisonService = Depends(get_comparison_service)
):
    return await service.compare_users(user1, user2)