快速开始
=========

本文档将指导您快速上手 Agent-Skill-MCP Framework。

系统要求
---------

- Python 3.9+
- pip 21.0+

安装框架
---------

1. 克隆仓库

   .. code-block:: bash

      git clone https://github.com/your-org/agent-skill-mcp-framework.git
      cd agent-skill-mcp-framework

2. 安装依赖

   .. code-block:: bash

      pip install -r requirements.txt

3. 安装框架

   .. code-block:: bash

      pip install -e .

配置环境
---------

在项目根目录创建 ``.env`` 文件，配置必要的环境变量：

.. code-block:: env

   # OpenAI API配置
   OPENAI_API_KEY=your-openai-api-key
   OPENAI_API_BASE=https://api.openai.com/v1

   # 日志配置
   LOG_LEVEL=INFO
   LOG_FILE=logs/app.log

   # 代理配置
   AGENT_NAME=DefaultAgent
   AGENT_TIMEOUT=30

运行示例
---------

框架提供了示例代码，展示如何使用核心功能：

.. code-block:: bash

   python src/examples/example_agent.py

示例代码将：
1. 创建一个代理实例
2. 添加示例技能
3. 执行技能
4. 使用MCP与大模型交互

下一步
-------

- 阅读 :doc:`core_concepts` 了解框架的核心概念
- 查看 :doc:`agent_development` 学习如何开发代理
- 参考 :doc:`skill_development` 学习如何创建自定义技能
- 阅读 :doc:`mcp_development` 了解如何扩展MCP实现
