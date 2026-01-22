from typing import Dict, Any, Optional, List
from agent_skill_mcp.core.skill import Skill
from agent_skill_mcp.exceptions import (
    SkillNotFoundError,
    SkillValidationError,
    SkillExecutionError,
    AgentTimeoutError
)
from agent_skill_mcp.logger import logger
from agent_skill_mcp.utils import timeout
from agent_skill_mcp.config import settings
import asyncio


class Agent:
    """代理类，负责管理技能和处理请求"""
    
    def __init__(self, name: Optional[str] = None):
        self.name = name or settings.agent.name
        self.skills: Dict[str, Skill] = {}
        self._running_tasks: Dict[str, asyncio.Task] = {}
        logger.info(f"Agent '{self.name}' initialized")
    
    def add_skill(self, skill: Skill) -> "Agent":
        """添加技能"""
        self.skills[skill.name] = skill
        logger.info(f"Added skill '{skill.name}' to agent '{self.name}'")
        return self
    
    def remove_skill(self, skill_name: str) -> "Agent":
        """移除技能"""
        if skill_name in self.skills:
            del self.skills[skill_name]
            logger.info(f"Removed skill '{skill_name}' from agent '{self.name}'")
        return self
    
    def get_skill(self, skill_name: str) -> Optional[Skill]:
        """获取技能"""
        return self.skills.get(skill_name)
    
    def get_all_skills(self) -> List[Skill]:
        """获取所有技能"""
        return list(self.skills.values())
    
    def get_skill_metadata(self, skill_name: str) -> Optional[Dict[str, Any]]:
        """获取技能元数据"""
        skill = self.get_skill(skill_name)
        if skill:
            return skill.get_metadata()
        return None
    
    def get_all_skill_metadata(self) -> List[Dict[str, Any]]:
        """获取所有技能元数据"""
        return [skill.get_metadata() for skill in self.get_all_skills()]
    
    @timeout(settings.agent.timeout)
    async def execute_skill(self, skill_name: str, params: Dict[str, Any]) -> Any:
        """执行技能"""
        logger.info(f"Executing skill '{skill_name}' with params: {params}")
        
        if skill_name not in self.skills:
            logger.error(f"Skill '{skill_name}' not found")
            raise SkillNotFoundError(skill_name)
        
        skill = self.skills[skill_name]
        
        # 验证参数
        if not skill.validate(params):
            logger.error(f"Invalid params for skill '{skill_name}': {params}")
            raise SkillValidationError(skill_name, "Invalid parameters")
        
        try:
            result = await skill.execute(params)
            logger.info(f"Skill '{skill_name}' executed successfully: {result}")
            return result
        except Exception as e:
            logger.error(f"Error executing skill '{skill_name}': {e}")
            raise SkillExecutionError(skill_name, str(e))
    
    def get_name(self) -> str:
        """获取代理名称"""
        return self.name
    
    def shutdown(self):
        """关闭代理"""
        logger.info(f"Shutting down agent '{self.name}'")
        # 取消所有运行中的任务
        for task_id, task in self._running_tasks.items():
            if not task.done():
                task.cancel()
        self._running_tasks.clear()
        logger.info(f"Agent '{self.name}' shutdown completed")
