from pydantic import BaseModel, Field

class StringToExcelRequest(BaseModel):
    text: str = Field(..., description="待处理的字符串，按空格分割")
    column_name: str = Field("内部订单号", description="Excel 列名")
    title: str = Field("售后单", description="下载文件名（不含扩展名）")