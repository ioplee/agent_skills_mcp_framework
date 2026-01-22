from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from agent_skill_mcp.exceptions import SkillValidationError


class SkillParams(BaseModel):
    """技能参数基类"""
    pass


class Skill(ABC):
    """技能基类"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """技能名称"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """技能描述"""
        pass
    
    @property
    def version(self) -> str:
        """技能版本"""
        return "1.0.0"
    
    @property
    def author(self) -> str:
        """技能作者"""
        return "Unknown"
    
    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> Any:
        """执行技能"""
        pass
    
    def validate(self, params: Dict[str, Any]) -> bool:
        """验证参数"""
        return True
    
    def get_metadata(self) -> Dict[str, Any]:
        """获取技能元数据"""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "author": self.author
        }
