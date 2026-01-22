import pytest
from agent_skill_mcp.skills.example_skill import ExampleSkill


@pytest.mark.asyncio
async def test_example_skill_initialization():
    """测试示例技能初始化"""
    skill = ExampleSkill()
    assert skill.name == "example"
    assert skill.description == "示例技能，返回输入的内容"
    assert skill.version == "1.0.0"
    assert skill.author == "Framework Team"


@pytest.mark.asyncio
async def test_example_skill_execute():
    """测试示例技能执行"""
    skill = ExampleSkill()
    params = {"content": "Test content"}
    result = await skill.execute(params)
    assert result["result"] == params["content"]
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_example_skill_execute_without_content():
    """测试示例技能执行（无content参数）"""
    skill = ExampleSkill()
    params = {}
    result = await skill.execute(params)
    assert result["result"] == "Hello, World!"
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_example_skill_validate():
    """测试示例技能参数验证"""
    skill = ExampleSkill()
    # 有效参数
    assert skill.validate({"content": "Test"}) is True
    # 无content参数
    assert skill.validate({}) is True
    # 无效参数类型
    assert skill.validate({"content": 123}) is False


@pytest.mark.asyncio
async def test_example_skill_get_metadata():
    """测试示例技能获取元数据"""
    skill = ExampleSkill()
    metadata = skill.get_metadata()
    assert metadata["name"] == skill.name
    assert metadata["description"] == skill.description
    assert metadata["version"] == skill.version
    assert metadata["author"] == skill.author
