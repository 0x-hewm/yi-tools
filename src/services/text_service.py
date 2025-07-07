"""
Text processing service
"""
from typing import Dict, Any


class TextService:
    """文本处理服务"""
    
    @staticmethod
    def process_text(text: str, operation: str) -> str | list[str]:
        """处理文本"""
        if operation == "uppercase":
            return text.upper()
        elif operation == "lowercase":
            return text.lower()
        elif operation == "reverse":
            return text[::-1]
        elif operation == "capitalize":
            return text.capitalize()
        elif operation == "title":
            return text.title()
        elif operation == "split":
            return text.split()
        else:
            return text
    
    @staticmethod
    def count_words(text: str) -> int:
        """统计单词数量"""
        return len(text.split())
    
    @staticmethod
    def count_characters(text: str, include_spaces: bool = True) -> int:
        """统计字符数量"""
        if include_spaces:
            return len(text)
        else:
            return len(text.replace(" ", ""))
