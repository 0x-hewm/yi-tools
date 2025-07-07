"""
Core configuration for yi-tools
"""
import os
from typing import Optional


class Settings:
    """应用程序设置"""
    def __init__(self):
        self.app_name: str = "yi-tools"
        self.app_version: str = "0.1.0"
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"
        self.host: str = os.getenv("HOST", "127.0.0.1")
        self.port: int = int(os.getenv("PORT", "8000"))
        
        # API 设置
        self.api_prefix: str = "/api/v1"
        self.docs_url: str = "/docs"
        self.redoc_url: str = "/redoc"
        self.openapi_url: str = "/openapi.json"


# 全局设置实例
settings = Settings()
