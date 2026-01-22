from typing import Dict, Any, List, Optional
from agent_skill_mcp.mcp import MCP, OpenAIMCP
from agent_skill_mcp.logger import logger
from agent_skill_mcp.config import settings


class MCPService:
    """模型控制协议服务"""
    
    def __init__(self):
        self._mcp: Optional[MCP] = None
    
    def initialize(self, api_key: Optional[str] = None, api_base: Optional[str] = None) -> MCP:
        """初始化MCP"""
        if self._mcp is None:
            self._mcp = OpenAIMCP(api_key, api_base)
            logger.info(f"Initialized MCP: {self._mcp.name} v{self._mcp.version}")
        return self._mcp
    
    def get_mcp(self) -> Optional[MCP]:
        """获取MCP实例"""
        return self._mcp
    
    async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
        """生成文本"""
        if self._mcp is None:
            self.initialize()
        return await self._mcp.generate(prompt, options)
    
    async def chat(self, messages: List[Dict[str, str]], options: Dict[str, Any] = None) -> str:
        """对话"""
        if self._mcp is None:
            self.initialize()
        return await self._mcp.chat(messages, options)
    
    async def embed(self, text: str, options: Dict[str, Any] = None) -> List[float]:
        """生成嵌入"""
        if self._mcp is None:
            self.initialize()
        return await self._mcp.embed(text, options)
    
    def close(self):
        """关闭MCP"""
        if self._mcp:
            self._mcp.close()
            self._mcp = None
            logger.info("Closed MCP")
