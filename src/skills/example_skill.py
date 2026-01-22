from typing import Dict, Any
from agent_skill_mcp.core.skill import Skill
from agent_skill_mcp.logger import logger


class ExampleSkill(Skill):
    """示例技能"""
    
    @property
    def name(self) -> str:
        """技能名称"""
        return "example"
    
    @property
    def description(self) -> str:
        """技能描述"""
        return "示例技能，返回输入的内容"
    
    @property
    def version(self) -> str:
        """技能版本"""
        return "1.0.0"
    
    @property
    def author(self) -> str:
        """技能作者"""
        return "Framework Team"
    
    async def execute(self, params: Dict[str, Any]) -> Any:
        """执行技能"""
        logger.info(f"Executing ExampleSkill with params: {params}")
        content = params.get("content", "Hello, World!")
        return {
            "result": content,
            "status": "success",
            "timestamp": "2026-01-22"
        }
    
    def validate(self, params: Dict[str, Any]) -> bool:
        """验证参数"""
        if "content" in params and not isinstance(params["content"], str):
            return False
        return True
