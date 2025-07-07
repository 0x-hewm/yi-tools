"""
Utility functions for yi-tools
"""
import hashlib
import uuid
from datetime import datetime
from typing import Any, Dict


def generate_uuid() -> str:
    """生成 UUID"""
    return str(uuid.uuid4())


def generate_timestamp() -> str:
    """生成时间戳"""
    return datetime.now().isoformat()


def hash_text(text: str, algorithm: str = "md5") -> str:
    """对文本进行哈希"""
    if algorithm == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")


def validate_email(email: str) -> bool:
    """简单的邮箱验证"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def format_file_size(size_bytes: int) -> str:
    """格式化文件大小"""
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    size = float(size_bytes)
    while size >= 1024 and i < len(size_names) - 1:
        size /= 1024
        i += 1
    
    return f"{size:.2f}{size_names[i]}"
