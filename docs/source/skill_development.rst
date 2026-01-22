技能开发指南
=============

本文档介绍如何开发自定义技能，扩展 Agent-Skill-MCP Framework 的功能。

创建自定义技能
--------------

要创建自定义技能，需要继承 ``Skill`` 基类并实现必要的方法：

.. code-block:: python

   from typing import Dict, Any
   from agent_skill_mcp.core.skill import Skill

   class CustomSkill(Skill):
       """自定义技能"""
       
       @property
       def name(self) -> str:
           """技能名称"""
           return "custom"
       
       @property
       def description(self) -> str:
           """技能描述"""
           return "自定义技能示例"
       
       @property
       def version(self) -> str:
           """技能版本"""
           return "1.0.0"
       
       @property
       def author(self) -> str:
           """技能作者"""
           return "Your Name"
       
       async def execute(self, params: Dict[str, Any]) -> Any:
           """执行技能"""
           # 技能的核心逻辑
           return {
               "result": "Custom skill executed",
               "params": params
           }
       
       def validate(self, params: Dict[str, Any]) -> bool:
           """验证参数"""
           # 参数验证逻辑
           return True

实现技能的必要方法
------------------

创建自定义技能时，需要实现以下必要方法：

1. **name 属性**：返回技能的唯一标识符
2. **description 属性**：返回技能的功能描述
3. **execute 方法**：实现技能的核心逻辑，处理输入参数并返回结果

以下方法是可选的：

1. **version 属性**：返回技能的版本号，默认为 "1.0.0"
2. **author 属性**：返回技能的作者，默认为 "Unknown"
3. **validate 方法**：验证输入参数的有效性，默认为返回 True
4. **get_metadata 方法**：返回技能的元数据，默认为包含名称、描述、版本、作者

技能的参数验证
--------------

技能可以实现 ``validate`` 方法来验证输入参数的有效性：

.. code-block:: python

   def validate(self, params: Dict[str, Any]) -> bool:
       """验证参数"""
       # 检查必要参数
       if "required_param" not in params:
           return False
       
       # 检查参数类型
       if not isinstance(params.get("number_param"), int):
           return False
       
       return True

技能的异常处理
--------------

技能在执行过程中可能会遇到各种异常，建议在 ``execute`` 方法中适当处理异常：

.. code-block:: python

   async def execute(self, params: Dict[str, Any]) -> Any:
       """执行技能"""
       try:
           # 技能的核心逻辑
           result = await self._do_something(params)
           return {"result": result}
       except Exception as e:
           # 记录异常并返回错误信息
           from agent_skill_mcp.logger import logger
           logger.error(f"Error executing skill: {e}")
           raise

技能的元数据
------------

技能的元数据包含技能的基本信息，便于代理管理和使用技能：

.. code-block:: python

   def get_metadata(self) -> Dict[str, Any]:
       """获取技能元数据"""
       return {
           "name": self.name,
           "description": self.description,
           "version": self.version,
           "author": self.author,
           "requirements": ["requests>=2.31.0"],  # 自定义元数据
           "tags": ["custom", "example"]  # 自定义元数据
       }

注册技能到代理
--------------

创建自定义技能后，需要将其注册到代理中才能使用：

.. code-block:: python

   import asyncio
   from agent_skill_mcp.core import Agent
   from my_skills.custom_skill import CustomSkill

   async def main():
       # 创建代理
       agent = Agent("MyAgent")
       
       # 创建并添加自定义技能
       custom_skill = CustomSkill()
       agent.add_skill(custom_skill)
       
       # 执行自定义技能
       params = {"required_param": "value", "number_param": 42}
       result = await agent.execute_skill("custom", params)
       print(result)

   # 运行异步函数
   asyncio.run(main())

技能开发最佳实践
--------------

1. **单一职责**：每个技能应该只负责一个具体的功能
2. **参数验证**：实现 validate 方法，确保输入参数的有效性
3. **异常处理**：适当处理执行过程中的异常，提供清晰的错误信息
4. **元数据完整**：提供完整的技能元数据，便于管理和使用
5. **文档完善**：为技能添加详细的文档，说明其功能和使用方法
6. **测试覆盖**：为技能编写单元测试，确保其功能正常

通过遵循这些最佳实践，可以开发出高质量、可靠的技能，为框架添加丰富的功能。
