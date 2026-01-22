代理开发指南
=============

本文档介绍如何开发和使用 Agent（代理）组件。

创建代理
---------

要创建一个代理实例，只需导入 ``Agent`` 类并实例化：

.. code-block:: python

   from agent_skill_mcp.core import Agent

   # 创建代理，指定名称
   agent = Agent("MyAgent")
   
   # 获取代理名称
   print(agent.get_name())  # 输出: MyAgent

管理技能
---------

代理可以添加、移除、获取技能：

.. code-block:: python

   from agent_skill_mcp.core import Agent
   from agent_skill_mcp.skills.example_skill import ExampleSkill

   # 创建代理
   agent = Agent("MyAgent")
   
   # 创建技能
   example_skill = ExampleSkill()
   
   # 添加技能
   agent.add_skill(example_skill)
   
   # 移除技能
   # agent.remove_skill(example_skill.name)
   
   # 获取技能
   skill = agent.get_skill(example_skill.name)
   
   # 获取所有技能
   skills = agent.get_all_skills()

执行技能
---------

代理可以执行技能并获取执行结果：

.. code-block:: python

   import asyncio
   from agent_skill_mcp.core import Agent
   from agent_skill_mcp.skills.example_skill import ExampleSkill

   async def main():
       # 创建代理
       agent = Agent("MyAgent")
       
       # 添加技能
       example_skill = ExampleSkill()
       agent.add_skill(example_skill)
       
       # 执行技能
       params = {"content": "Hello, Agent!"}
       result = await agent.execute_skill("example", params)
       print(result)

   # 运行异步函数
   asyncio.run(main())

获取技能元数据
--------------

代理可以获取技能的元数据，了解技能的详细信息：

.. code-block:: python

   from agent_skill_mcp.core import Agent
   from agent_skill_mcp.skills.example_skill import ExampleSkill

   # 创建代理
   agent = Agent("MyAgent")
   
   # 添加技能
   example_skill = ExampleSkill()
   agent.add_skill(example_skill)
   
   # 获取单个技能的元数据
   metadata = agent.get_skill_metadata("example")
   print(metadata)
   
   # 获取所有技能的元数据
   all_metadata = agent.get_all_skill_metadata()
   for meta in all_metadata:
       print(meta)

异常处理
---------

代理在执行技能时会处理各种异常：

.. code-block:: python

   import asyncio
   from agent_skill_mcp.core import Agent
   from agent_skill_mcp.exceptions import SkillNotFoundError, SkillExecutionError

   async def main():
       # 创建代理
       agent = Agent("MyAgent")
       
       try:
           # 尝试执行不存在的技能
           await agent.execute_skill("non_existent", {})
       except SkillNotFoundError as e:
           print(f"技能未找到: {e}")
       
       try:
           # 尝试执行技能时传入无效参数
           await agent.execute_skill("example", {"content": 123})  # 无效参数类型
       except SkillExecutionError as e:
           print(f"技能执行错误: {e}")

   # 运行异步函数
   asyncio.run(main())

关闭代理
---------

当代理不再需要时，可以关闭它：

.. code-block:: python

   from agent_skill_mcp.core import Agent

   # 创建代理
   agent = Agent("MyAgent")
   
   # 使用代理...
   
   # 关闭代理
   agent.shutdown()

代理的高级特性
-------------

- **超时控制**：代理执行技能时会应用超时限制，防止技能执行时间过长
- **日志记录**：代理会记录所有操作的日志，便于调试和监控
- **技能管理**：代理可以动态管理技能，支持运行时添加和移除技能

通过合理使用代理的特性，可以构建功能强大、可靠的大模型应用。
