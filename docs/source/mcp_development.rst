MCP 开发指南
=============

本文档介绍如何开发和扩展 MCP（Model Control Protocol），为 Agent-Skill-MCP Framework 添加新的模型交互能力。

MCP 简介
--------

MCP（Model Control Protocol）是框架与大模型交互的标准化接口，它定义了：

- **生成文本**：根据提示生成文本内容
- **对话**：处理多轮对话
- **生成嵌入**：将文本转换为向量表示
- **管理连接**：处理与模型服务的连接和认证

通过实现 MCP 接口，可以让框架支持不同的大模型服务。

实现自定义 MCP
--------------

要实现自定义 MCP，需要继承 ``MCP`` 基类并实现必要的方法：

.. code-block:: python

   from typing import Dict, Any, List
   from agent_skill_mcp.mcp import MCP

   class CustomMCP(MCP):
       """自定义MCP实现"""
       
       def __init__(self, api_key: str, base_url: str = "https://api.example.com/v1"):
           self.api_key = api_key
           self.base_url = base_url
           # 初始化连接等
       
       @property
       def name(self) -> str:
           """MCP名称"""
           return "CustomMCP"
       
       @property
       def version(self) -> str:
           """MCP版本"""
           return "1.0.0"
       
       async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
           """生成文本"""
           # 实现文本生成逻辑
           return "Generated text"
       
       async def chat(self, messages: List[Dict[str, str]], options: Dict[str, Any] = None) -> str:
           """对话"""
           # 实现对话逻辑
           return "Chat response"
       
       async def embed(self, text: str, options: Dict[str, Any] = None) -> List[float]:
           """生成嵌入"""
           # 实现嵌入生成逻辑
           return [0.1, 0.2, 0.3]
       
       def close(self):
           """关闭连接"""
           # 清理资源
           pass

实现 MCP 的必要方法
------------------

创建自定义 MCP 时，需要实现以下必要方法：

1. **name 属性**：返回 MCP 的名称
2. **version 属性**：返回 MCP 的版本号
3. **generate 方法**：根据提示生成文本
4. **chat 方法**：处理多轮对话
5. **embed 方法**：生成文本的嵌入向量
6. **close 方法**：关闭连接，清理资源

MCP 的异常处理
--------------

MCP 实现中应该适当处理异常，特别是网络请求和认证相关的异常：

.. code-block:: python

   from agent_skill_mcp.exceptions import (
       MCPError,
       MCPConnectionError,
       MCPAuthenticationError,
       MCPTimeoutError
   )

   async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
       """生成文本"""
       try:
           # 发送请求
           response = await self._send_request("generate", {"prompt": prompt, **options})
           return response
       except requests.exceptions.Timeout:
           raise MCPTimeoutError("Request timed out")
       except requests.exceptions.ConnectionError:
           raise MCPConnectionError("Connection error")
       except Exception as e:
           raise MCPError(f"Error generating text: {str(e)}")

MCP 的配置管理
--------------

MCP 实现可以使用框架的配置管理系统，获取配置参数：

.. code-block:: python

   from agent_skill_mcp.config import settings

   def __init__(self, api_key: str = None, base_url: str = None):
       self.api_key = api_key or settings.custom_api_key
       self.base_url = base_url or settings.custom_api_base

MCP 的重试机制
--------------

MCP 实现可以使用框架的重试装饰器，提高请求的可靠性：

.. code-block:: python

   from agent_skill_mcp.utils import retry

   @retry(max_attempts=3, delay=1.0, backoff=2.0)
   async def generate(self, prompt: str, options: Dict[str, Any] = None) -> str:
       """生成文本"""
       # 实现文本生成逻辑
       pass

使用自定义 MCP
--------------

创建自定义 MCP 后，可以在代码中使用它：

.. code-block:: python

   import asyncio
   from agent_skill_mcp.mcp import CustomMCP

   async def main():
       # 初始化 MCP
       mcp = CustomMCP("your-api-key")
       
       # 生成文本
       text = await mcp.generate("Write a short story")
       print(text)
       
       # 对话
       messages = [
           {"role": "user", "content": "Hello"}
       ]
       response = await mcp.chat(messages)
       print(response)
       
       # 生成嵌入
       embedding = await mcp.embed("Test text")
       print(len(embedding))
       
       # 关闭 MCP
       mcp.close()

   # 运行异步函数
   asyncio.run(main())

MCP 开发最佳实践
--------------

1. **异常处理**：适当处理各种异常，特别是网络和认证相关的异常
2. **重试机制**：对网络请求实现重试机制，提高可靠性
3. **超时控制**：为请求设置合理的超时时间
4. **配置管理**：使用框架的配置管理系统，提高可配置性
5. **日志记录**：记录关键操作和错误信息，便于调试
6. **资源管理**：正确管理网络连接等资源，避免资源泄漏
7. **统一接口**：严格按照 MCP 接口定义实现方法，确保兼容性

通过遵循这些最佳实践，可以开发出高质量、可靠的 MCP 实现，为框架添加新的模型支持。
