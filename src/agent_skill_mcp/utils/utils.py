import json
import time
from typing import Dict, Any, Optional
import asyncio
from functools import wraps


def json_serialize(obj: Any) -> str:
    """JSON序列化"""
    return json.dumps(obj, ensure_ascii=False, indent=2)


def json_deserialize(s: str) -> Any:
    """JSON反序列化"""
    return json.loads(s)


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    await asyncio.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator


def timeout(seconds: int):
    """超时装饰器"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await asyncio.wait_for(func(*args, **kwargs), timeout=seconds)
            except asyncio.TimeoutError:
                from agent_skill_mcp.exceptions import AgentTimeoutError
                raise AgentTimeoutError(f"Operation timed out after {seconds} seconds")
        return wrapper
    return decorator


def validate_params(params: Dict[str, Any], required: list = None, types: Dict[str, type] = None) -> bool:
    """验证参数"""
    if required:
        for param in required:
            if param not in params:
                return False
    
    if types:
        for param, expected_type in types.items():
            if param in params and not isinstance(params[param], expected_type):
                return False
    
    return True


def generate_unique_id() -> str:
    """生成唯一ID"""
    return f"{int(time.time() * 1000)}-{hash(time.time()) % 10000}"
