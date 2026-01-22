from pydantic_settings import BaseSettings
from typing import Optional


class OpenAISettings(BaseSettings):
    """OpenAI API配置"""
    api_key: str
    api_base: str = "https://api.openai.com/v1"
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 150
    temperature: float = 0.7

    class Config:
        env_prefix = "OPENAI_"


class LogSettings(BaseSettings):
    """日志配置"""
    level: str = "INFO"
    file: Optional[str] = None
    rotation: str = "10 MB"
    retention: str = "7 days"

    class Config:
        env_prefix = "LOG_"


class AgentSettings(BaseSettings):
    """代理配置"""
    name: str = "DefaultAgent"
    timeout: int = 30

    class Config:
        env_prefix = "AGENT_"


class Settings(BaseSettings):
    """全局配置"""
    openai: OpenAISettings
    log: LogSettings = LogSettings()
    agent: AgentSettings = AgentSettings()
    debug: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# 创建全局配置实例
settings = Settings()
