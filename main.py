"""
Entry point for yi-tools application
"""
import uvicorn
from src.app import app
from src.core.config import Settings

settings = Settings()


def main():
    """启动 FastAPI 应用"""
    print(f"启动 {settings.app_name} v{settings.app_version}")
    print(f"服务器地址: http://{settings.host}:{settings.port}")
    print(f"API 文档: http://{settings.host}:{settings.port}{settings.docs_url}")
    
    uvicorn.run(
        "src.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )


if __name__ == "__main__":
    main()
