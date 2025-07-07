"""
Tools routes for various utility functions
"""
import io

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import pandas as pd
from typing import Dict, Any
from src.services.text_service import TextService
from src.utils.helpers import generate_uuid, generate_timestamp, hash_text
from src.api.schemas import tools
from urllib.parse import quote

router = APIRouter(prefix="/tools", tags=["tools"])


@router.get("/")
async def list_tools():
    """列出所有可用的工具"""
    return {
        "tools": [
            {"name": "string-to-excel-column", "description": "字符串转单列 Excel"}
        ]
    }

@router.post(
        "/string-to-excel-column",
        summary="字符串转单列 Excel",
        description="将空格分割的字符串转换为单列 Excel 文件并下载",
        response_class=StreamingResponse,
        responses={
            200: {
                "content": {"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": {}},
                "description": "Excel 文件流"
            }
        }
    )
async def string_to_excel_column(data: tools.StringToExcelRequest):
    """空格分割的字符串转单列 Excel 表格"""
    result = TextService.process_text(data.text, "split")
    df = pd.DataFrame({data.column_name: result})
    output = io.BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    filename = quote(f"{data.title}.xlsx")

    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers= {"Content-Disposition": f"attachment; filename*=UTF-8''{filename}"}
    )