from typing import List, Dict, Any, Optional
from agent_skill_mcp.core import Agent
from agent_skill_mcp.core.skill import Skill
from agent_skill_mcp.logger import logger


class SkillService:
    """技能管理服务"""
    
    def __init__(self):
        self._agent = Agent("SkillServiceAgent")
        self._skills: Dict[str, Skill] = {}
    
    def register_skill(self, skill: Skill) -> bool:
        """注册技能"""
        if skill.name in self._skills:
            logger.warning(f"Skill {skill.name} already registered")
            return False
        
        self._skills[skill.name] = skill
        self._agent.add_skill(skill)
        logger.info(f"Registered skill: {skill.name}")
        return True
    
    def unregister_skill(self, skill_name: str) -> bool:
        """注销技能"""
        if skill_name not in self._skills:
            logger.warning(f"Skill {skill_name} not found")
            return False
        
        del self._skills[skill_name]
        self._agent.remove_skill(skill_name)
        logger.info(f"Unregistered skill: {skill_name}")
        return True
    
    def get_skill(self, skill_name: str) -> Optional[Skill]:
        """获取技能"""
        return self._skills.get(skill_name)
    
    def get_all_skills(self) -> List[Skill]:
        """获取所有技能"""
        return list(self._skills.values())
    
    def get_skill_metadata(self, skill_name: str) -> Optional[Dict[str, Any]]:
        """获取技能元数据"""
        return self._agent.get_skill_metadata(skill_name)
    
    def get_all_skill_metadata(self) -> List[Dict[str, Any]]:
        """获取所有技能元数据"""
        return self._agent.get_all_skill_metadata()
    
    async def execute_skill(self, skill_name: str, params: Dict[str, Any]) -> Any:
        """执行技能"""
        return await self._agent.execute_skill(skill_name, params)
