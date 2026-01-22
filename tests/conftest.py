import pytest
import os
from unittest.mock import Mock, patch


@pytest.fixture
def mock_env_vars():
    """模拟环境变量"""
    with patch.dict(os.environ, {
        "OPENAI_API_KEY": "test-api-key",
        "OPENAI_API_BASE": "https://api.openai.com/v1",
        "LOG_LEVEL": "ERROR",
        "AGENT_NAME": "TestAgent"
    }):
        yield


@pytest.fixture
def mock_openai_response():
    """模拟OpenAI API响应"""
    return {
        "completions": {
            "choices": [{
                "text": "Test completion"
            }]
        },
        "chat/completions": {
            "choices": [{
                "message": {
                    "content": "Test chat response"
                }
            }]
        },
        "embeddings": {
            "data": [{
                "embedding": [0.1, 0.2, 0.3]
            }]
        }
    }
