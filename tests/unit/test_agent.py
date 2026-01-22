import pytest
from agent_skill_mcp.core import Agent
from agent_skill_mcp.skills.example_skill import ExampleSkill
from agent_skill_mcp.exceptions import SkillNotFoundError, SkillExecutionError


@pytest.mark.asyncio
async def test_agent_initialization():
    """测试代理初始化"""
    agent = Agent("TestAgent")
    assert agent.get_name() == "TestAgent"


@pytest.mark.asyncio
async def test_agent_add_skill():
    """测试添加技能"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    assert len(agent.get_all_skills()) == 1
    assert agent.get_skill(skill.name) is skill


@pytest.mark.asyncio
async def test_agent_remove_skill():
    """测试移除技能"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    assert len(agent.get_all_skills()) == 1
    agent.remove_skill(skill.name)
    assert len(agent.get_all_skills()) == 0
    assert agent.get_skill(skill.name) is None


@pytest.mark.asyncio
async def test_agent_execute_skill():
    """测试执行技能"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    
    params = {"content": "Test content"}
    result = await agent.execute_skill(skill.name, params)
    assert result["result"] == params["content"]


@pytest.mark.asyncio
async def test_agent_execute_nonexistent_skill():
    """测试执行不存在的技能"""
    agent = Agent("TestAgent")
    with pytest.raises(SkillNotFoundError):
        await agent.execute_skill("nonexistent", {})


@pytest.mark.asyncio
async def test_agent_get_skill_metadata():
    """测试获取技能元数据"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    
    metadata = agent.get_skill_metadata(skill.name)
    assert metadata is not None
    assert metadata["name"] == skill.name
    assert metadata["version"] == skill.version


@pytest.mark.asyncio
async def test_agent_get_all_skill_metadata():
    """测试获取所有技能元数据"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    
    metadata_list = agent.get_all_skill_metadata()
    assert len(metadata_list) == 1
    assert metadata_list[0]["name"] == skill.name
