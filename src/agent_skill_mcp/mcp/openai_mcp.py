import requests
from typing import Dict, Any, List, Optional
from agent_skill_mcp.mcp.mcp import MCP
from agent_skill_mcp.config import settings
from agent_skill_mcp.logger import logger
from agent_skill_mcp.exceptions import (
    MCPError,
    MCPConnectionError,
    MCPAuthenticationError,
    MCPTimeoutError
)
from agent_skill_mcp.utils import retry


class OpenAIMCP(MCP):
    """OpenAI MCP实现"""
    
    def __init__(self, api_key: Optional[str] = None, api_base: Optional[str] = None):
        self.api_key = api_key or settings.openai.api_key
        self.api_base = api_base or settings.openai.api_base
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        logger.info(f"OpenAIMCP initialized with base URL: {self.api_base}")
    
    @property
    def name(self) -> str:
        """MCP名称"""
        return "OpenAIMCP"
    
    @property
    def version(self) -> str:
        """MCP版本"""
        return "1.0.0"
    
    @retry(max_attempts=3, delay=1.0, backoff=2.0)
    async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
        """生成文本"""
        logger.debug(f"Generating text with prompt: {prompt[:100]}...")
        
        if options is None:
            options = {}
        
        payload = {
            "model": options.get("model", settings.openai.model),
            "prompt": prompt,
            "max_tokens": options.get("max_tokens", settings.openai.max_tokens),
            "temperature": options.get("temperature", settings.openai.temperature),
            **options
        }
        
        try:
            response = requests.post(
                f"{self.api_base}/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 401:
                raise MCPAuthenticationError("Invalid API key")
            elif response.status_code >= 500:
                raise MCPConnectionError(f"OpenAI API error: {response.status_code}")
            elif response.status_code != 200:
                raise MCPError(f"OpenAI API error: {response.status_code}, {response.text}")
            
            result = response.json()
            text = result["choices"][0]["text"].strip()
            logger.debug(f"Generated text: {text[:100]}...")
            return text
        except requests.exceptions.Timeout:
            raise MCPTimeoutError("OpenAI API request timed out")
        except requests.exceptions.ConnectionError:
            raise MCPConnectionError("Failed to connect to OpenAI API")
        except Exception as e:
            raise MCPError(f"Error generating text: {str(e)}")
    
    @retry(max_attempts=3, delay=1.0, backoff=2.0)
    async def chat(self, messages: List[Dict[str, str]], options: Dict[str, Any] = None) -> str:
        """对话"""
        logger.debug(f"Chatting with messages: {messages}")
        
        if options is None:
            options = {}
        
        payload = {
            "model": options.get("model", settings.openai.model),
            "messages": messages,
            "max_tokens": options.get("max_tokens", settings.openai.max_tokens),
            "temperature": options.get("temperature", settings.openai.temperature),
            **options
        }
        
        try:
            response = requests.post(
                f"{self.api_base}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 401:
                raise MCPAuthenticationError("Invalid API key")
            elif response.status_code >= 500:
                raise MCPConnectionError(f"OpenAI API error: {response.status_code}")
            elif response.status_code != 200:
                raise MCPError(f"OpenAI API error: {response.status_code}, {response.text}")
            
            result = response.json()
            text = result["choices"][0]["message"]["content"].strip()
            logger.debug(f"Chat response: {text[:100]}...")
            return text
        except requests.exceptions.Timeout:
            raise MCPTimeoutError("OpenAI API request timed out")
        except requests.exceptions.ConnectionError:
            raise MCPConnectionError("Failed to connect to OpenAI API")
        except Exception as e:
            raise MCPError(f"Error chatting: {str(e)}")
    
    @retry(max_attempts=3, delay=1.0, backoff=2.0)
    async def embed(self, text: str, options: Dict[str, Any] = None) -> List[float]:
        """生成嵌入"""
        logger.debug(f"Generating embedding for text: {text[:100]}...")
        
        payload = {
            "model": "text-embedding-ada-002",
            "input": text
        }
        
        if options:
            payload.update(options)
        
        try:
            response = requests.post(
                f"{self.api_base}/embeddings",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 401:
                raise MCPAuthenticationError("Invalid API key")
            elif response.status_code >= 500:
                raise MCPConnectionError(f"OpenAI API error: {response.status_code}")
            elif response.status_code != 200:
                raise MCPError(f"OpenAI API error: {response.status_code}, {response.text}")
            
            result = response.json()
            embedding = result["data"][0]["embedding"]
            logger.debug(f"Generated embedding with length: {len(embedding)}")
            return embedding
        except requests.exceptions.Timeout:
            raise MCPTimeoutError("OpenAI API request timed out")
        except requests.exceptions.ConnectionError:
            raise MCPConnectionError("Failed to connect to OpenAI API")
        except Exception as e:
            raise MCPError(f"Error generating embedding: {str(e)}")
    
    def close(self):
        """关闭连接"""
        logger.info("Closing OpenAIMCP connection")
        # OpenAI API doesn't require closing connections
        pass
