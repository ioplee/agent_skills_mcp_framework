import pytest
import asyncio
from agent_skill_mcp.utils import utils


@pytest.mark.asyncio
async def test_json_serialize_deserialize():
    """测试JSON序列化和反序列化"""
    test_obj = {"key": "value", "number": 42, "list": [1, 2, 3]}
    serialized = utils.json_serialize(test_obj)
    deserialized = utils.json_deserialize(serialized)
    assert deserialized == test_obj


@pytest.mark.asyncio
async def test_retry_decorator():
    """测试重试装饰器"""
    counter = 0
    
    @utils.retry(max_attempts=3, delay=0.1, backoff=1)
    async def test_func():
        nonlocal counter
        counter += 1
        if counter < 3:
            raise ValueError("Test error")
        return "Success"
    
    result = await test_func()
    assert result == "Success"
    assert counter == 3


@pytest.mark.asyncio
async def test_timeout_decorator():
    """测试超时装饰器"""
    @utils.timeout(1)
    async def test_func():
        await asyncio.sleep(2)
        return "Success"
    
    from agent_skill_mcp.exceptions import AgentTimeoutError
    with pytest.raises(AgentTimeoutError):
        await test_func()


@pytest.mark.asyncio
async def test_validate_params():
    """测试参数验证"""
    # 测试必填参数
    params = {"name": "test", "age": 20}
    assert utils.validate_params(params, required=["name", "age"]) is True
    assert utils.validate_params(params, required=["name", "age", "email"]) is False
    
    # 测试参数类型
    types = {"name": str, "age": int}
    assert utils.validate_params(params, types=types) is True
    
    # 测试无效参数类型
    invalid_params = {"name": "test", "age": "20"}
    assert utils.validate_params(invalid_params, types=types) is False


@pytest.mark.asyncio
async def test_generate_unique_id():
    """测试生成唯一ID"""
    id1 = utils.generate_unique_id()
    id2 = utils.generate_unique_id()
    assert id1 != id2
    assert len(id1) > 0
