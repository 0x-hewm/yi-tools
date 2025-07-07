"""
API Router configuration
集中管理所有路由的注册
"""
from fastapi import APIRouter
from .routes import health, tools

# 创建主路由器
api_router = APIRouter()

# 注册所有路由
api_router.include_router(health.router)
api_router.include_router(tools.router)

# 导出以供主应用使用
__all__ = ["api_router"]
