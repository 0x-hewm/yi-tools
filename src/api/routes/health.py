"""
Health check and basic routes
"""
from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy", "message": "yi-tools is running!"}


@router.get("/version")
async def get_version():
    """获取版本信息"""
    return {"version": "0.1.0", "name": "yi-tools"}
