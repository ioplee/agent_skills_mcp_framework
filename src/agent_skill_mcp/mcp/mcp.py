from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class MCP(ABC):
    """Model Control Protocol 接口"""
    
    @abstractmethod
    async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
        """生成文本"""
        pass
    
    @abstractmethod
    async def chat(self, messages: List[Dict[str, str]], options: Dict[str, Any] = None) -> str:
        """对话"""
        pass
    
    @abstractmethod
    async def embed(self, text: str, options: Dict[str, Any] = None) -> List[float]:
        """生成嵌入"""
        pass
    
    @abstractmethod
    def close(self):
        """关闭连接"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """MCP名称"""
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        """MCP版本"""
        pass
