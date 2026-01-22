import pytest
from unittest.mock import Mock, patch
from agent_skill_mcp.core import Agent
from agent_skill_mcp.skills.example_skill import ExampleSkill
from agent_skill_mcp.mcp import OpenAIMCP


@pytest.mark.asyncio
async def test_agent_with_skill_integration():
    """测试代理与技能集成"""
    agent = Agent("TestAgent")
    skill = ExampleSkill()
    agent.add_skill(skill)
    
    # 测试技能执行
    params = {"content": "Integration test"}
    result = await agent.execute_skill(skill.name, params)
    assert result["result"] == params["content"]
    assert result["status"] == "success"


@pytest.mark.asyncio
@patch('requests.post')
async def test_mcp_integration(mock_post):
    """测试MCP集成"""
    # 模拟OpenAI API响应
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [{
            "text": "Test completion"
        }]
    }
    mock_post.return_value = mock_response
    
    # 测试MCP生成文本
    mcp = OpenAIMCP(api_key="test-key")
    result = await mcp.generate("Test prompt")
    assert result == "Test completion"
