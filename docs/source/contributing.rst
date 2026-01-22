贡献指南
=========

本文档介绍如何为 Agent-Skill-MCP Framework 贡献代码和改进。

开发环境设置
-------------

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

3. **安装开发依赖**

   .. code-block:: bash

      pip install -e .[dev]

4. **配置预提交钩子**

   .. code-block:: bash

      pre-commit install

开发流程
---------

1. **创建分支**

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. **编写代码**

   - 遵循项目的代码风格和命名约定
   - 为新功能添加适当的测试用例
   - 更新相关文档

3. **运行测试**

   .. code-block:: bash

      pytest

4. **运行代码质量检查**

   .. code-block:: bash

      # 运行 Black 代码格式化
      black src/

      # 运行 isort 导入排序
      isort src/

      # 运行 flake8 代码检查
      flake8 src/

      # 运行 mypy 类型检查
      mypy src/

5. **提交代码**

   .. code-block:: bash

      git add .
      git commit -m "Add your feature or fix"

6. **推送分支**

   .. code-block:: bash

      git push origin feature/your-feature-name

7. **创建拉取请求**

   在 GitHub 上创建拉取请求，描述您的更改和改进。

代码风格指南
-------------

1. **命名约定**

   - **模块名**：小写字母，单词之间用下划线分隔
   - **类名**：驼峰命名法（PascalCase）
   - **函数名**：小写字母，单词之间用下划线分隔
   - **变量名**：小写字母，单词之间用下划线分隔
   - **常量名**：全大写字母，单词之间用下划线分隔

2. **代码风格**

   - 使用 4 个空格进行缩进
   - 每行代码长度不超过 88 个字符
   - 使用双引号 "" 表示字符串
   - 导入语句按以下顺序排序：
     1. 标准库导入
     2. 第三方库导入
     3. 本地模块导入
   - 函数和类之间空两行
   - 函数内部不同逻辑块之间空一行

3. **文档字符串**

   使用 Google 风格的文档字符串：

   .. code-block:: python

      def function_name(param1, param2):
          """函数描述

          Args:
              param1: 参数1的描述
              param2: 参数2的描述

          Returns:
              返回值的描述

          Raises:
              ExceptionType: 异常的描述
          """
          pass

4. **类型提示**

   使用 Python 的类型提示：

   .. code-block:: python

      from typing import Dict, Any, List

      def process_data(data: Dict[str, Any]) -> List[str]:
          pass

测试指南
---------

1. **测试文件结构**

   - 单元测试：`tests/unit/` 目录
   - 集成测试：`tests/integration/` 目录

2. **测试命名约定**

   - 测试文件：`test_<module_name>.py`
   - 测试函数：`test_<function_name>`

3. **编写测试**

   使用 pytest 编写测试用例：

   .. code-block:: python

      import pytest

      def test_functionality():
          assert 1 + 1 == 2

4. **运行测试**

   .. code-block:: bash

      # 运行所有测试
      pytest

      # 运行特定测试文件
      pytest tests/unit/test_agent.py

      # 运行特定测试函数
      pytest tests/unit/test_agent.py::test_agent_initialization

文档指南
---------

1. **文档结构**

   - 快速开始：`docs/source/getting_started.rst`
   - 核心概念：`docs/source/core_concepts.rst`
   - 开发指南：`docs/source/*_development.rst`
   - API 参考：`docs/source/api_reference.rst`
   - 部署指南：`docs/source/deployment.rst`

2. **编写文档**

   使用 reStructuredText (reST) 格式编写文档：

   .. code-block:: rst

      标题
      =====

      段落文本。

      - 列表项 1
      - 列表项 2

3. **构建文档**

   .. code-block:: bash

      cd docs
      make html

   构建的文档位于 `docs/build/html/` 目录。

问题报告和功能请求
-----------------

如果您发现了问题或有功能请求，请在 GitHub 上创建 issue：

1. **问题报告**：
   - 描述问题的详细信息
   - 提供重现步骤
   - 包含相关的错误信息和日志
   - 说明您的环境（Python 版本、操作系统等）

2. **功能请求**：
   - 描述您希望添加的功能
   - 说明为什么这个功能很重要
   - 提供可能的实现方案

贡献类型
---------

我们欢迎以下类型的贡献：

1. **代码改进**：修复错误、优化性能、添加新功能
2. **文档更新**：改进现有文档、添加新文档
3. **测试用例**：添加新的测试用例，提高测试覆盖率
4. **bug 报告**：报告框架中的问题
5. **功能请求**：提出新的功能建议

感谢您对 Agent-Skill-MCP Framework 的贡献！
