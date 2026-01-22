部署指南
=========

本文档介绍如何部署和运行 Agent-Skill-MCP Framework。

环境准备
---------

在部署框架之前，需要准备以下环境：

- **操作系统**：Linux、macOS 或 Windows
- **Python**：3.9 或更高版本
- **依赖**：框架所需的 Python 包
- **API 密钥**：如果使用 OpenAI 等第三方服务，需要相应的 API 密钥

安装部署
---------

1. **克隆仓库**

   .. code-block:: bash

      git clone https://github.com/your-org/agent-skill-mcp-framework.git
      cd agent-skill-mcp-framework

2. **创建虚拟环境**

   .. code-block:: bash

      # Linux/macOS
      python3 -m venv venv
      source venv/bin/activate

      # Windows
      python -m venv venv
      venv\Scripts\activate

3. **安装依赖**

   .. code-block:: bash

      pip install -r requirements.txt

4. **安装框架**

   .. code-block:: bash

      pip install -e .

5. **配置环境变量**

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

6. **创建日志目录**

   .. code-block:: bash

      mkdir -p logs

运行框架
---------

### 运行示例

可以运行框架提供的示例代码，验证安装是否成功：

.. code-block:: bash

   python src/examples/example_agent.py

### 集成到项目中

将框架集成到您的项目中，使用以下步骤：

1. **导入框架模块**

   .. code-block:: python

      from agent_skill_mcp.core import Agent
      from agent_skill_mcp.mcp import OpenAIMCP

2. **创建代理和技能**

   .. code-block:: python

      # 创建代理
      agent = Agent("MyAgent")

      # 添加技能
      from my_skills import MySkill
      agent.add_skill(MySkill())

3. **执行技能**

   .. code-block:: python

      import asyncio

      async def main():
          result = await agent.execute_skill("my_skill", {"param": "value"})
          print(result)

      asyncio.run(main())

4. **使用 MCP**

   .. code-block:: python

      async def main():
          mcp = OpenAIMCP()
          response = await mcp.chat([{"role": "user", "content": "Hello"}])
          print(response)
          mcp.close()

      asyncio.run(main())

生产环境部署
-----------

在生产环境中部署框架，建议以下配置：

1. **使用系统服务**

   将框架作为系统服务运行，确保其在系统启动时自动运行：

   .. code-block:: bash

      # 创建系统服务文件
      sudo nano /etc/systemd/system/agent-skill-mcp.service

   服务文件内容：

   .. code-block:: ini

      [Unit]
      Description=Agent-Skill-MCP Framework
      After=network.target

      [Service]
      Type=simple
      User=your-user
      WorkingDirectory=/path/to/agent-skill-mcp-framework
      ExecStart=/path/to/venv/bin/python /path/to/agent-skill-mcp-framework/src/your-application.py
      Restart=always

      [Install]
      WantedBy=multi-user.target

2. **使用容器化部署**

   使用 Docker 容器化部署框架：

   .. code-block:: dockerfile

      FROM python:3.9-slim

      WORKDIR /app

      COPY . .

      RUN pip install -r requirements.txt
      RUN pip install -e .

      ENV OPENAI_API_KEY=your-openai-api-key
      ENV LOG_LEVEL=INFO

      CMD ["python", "src/your-application.py"]

3. **配置监控**

   在生产环境中，建议配置监控系统，监控框架的运行状态：

   - **日志监控**：使用 ELK Stack 或类似工具收集和分析日志
   - **指标监控**：使用 Prometheus 或类似工具监控性能指标
   - **告警系统**：配置告警规则，及时发现和处理异常

4. **安全配置**

   在生产环境中，注意以下安全配置：

   - **API 密钥管理**：使用密钥管理服务存储 API 密钥，避免硬编码
   - **网络安全**：配置适当的网络访问控制，限制不必要的网络访问
   - **权限控制**：设置适当的文件和目录权限，避免权限泄露

扩展和自定义
-------------

根据您的需求，可以扩展和自定义框架：

1. **添加自定义技能**：实现新的技能类，扩展框架的功能
2. **扩展 MCP 实现**：实现新的 MCP 类，支持更多的大模型服务
3. **修改配置管理**：根据需要调整配置管理系统
4. **定制日志系统**：根据需要调整日志系统的配置

通过合理的扩展和自定义，可以使框架更好地满足您的特定需求。
