# Agent-Skill-MCP 框架

基于agent-skill-mcp架构的企业级大模型开发框架。

## 项目结构

```
agent-skill-mcp-framework/
├── src/
│   ├── agent_skill_mcp/
│   │   ├── core/         # 核心组件
│   │   ├── mcp/          # 模型控制协议
│   │   ├── config/       # 配置管理
│   │   ├── utils/        # 工具函数
│   │   ├── logger/       # 日志系统
│   │   ├── exceptions/   # 异常处理
│   │   ├── services/     # 服务层
│   │   ├── cli/          # 命令行接口
│   │   ├── interfaces/   # API接口定义
│   │   └── middleware/   # 中间件
│   ├── skills/           # 技能实现
│   ├── examples/         # 示例代码
├── tests/                # 测试用例
├── docs/                 # 文档
├── scripts/              # 脚本工具
├── deploy/               # 部署配置
├── setup.py              # 包配置
├── requirements.txt      # 依赖文件
├── README.md             # 项目说明
└── .gitignore            # Git忽略文件
```

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 安装框架

```bash
pip install -e .
```

### 配置环境

复制环境变量模板文件并根据需要修改：

```bash
cp .env.example .env
# 编辑.env文件，设置您的配置
```

### 运行示例

```bash
python src/examples/example_agent.py
```

### 使用命令行接口

```bash
# 列出所有可用技能
agent-skill-mcp list-skills

# 执行指定技能
agent-skill-mcp execute --skill example --params '{"content": "Hello"}'

# 显示框架版本
agent-skill-mcp version
```

## 核心概念

- **Agent**: 代理，负责管理技能和处理请求
- **Skill**: 技能，封装特定功能的可执行单元
- **MCP**: Model Control Protocol，模型控制协议，负责与大模型交互
- **Service**: 服务，提供高级功能封装，如技能管理和MCP服务
- **CLI**: 命令行接口，提供命令行操作功能

## 配置管理

框架使用环境变量和配置文件进行配置管理。在项目根目录创建 `.env` 文件：

```env
# OpenAI API配置
OPENAI_API_KEY=your-openai-api-key
OPENAI_API_BASE=https://api.openai.com/v1

# 日志配置
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# 代理配置
AGENT_NAME=DefaultAgent
```

## 开发指南

### 创建自定义技能

1. 继承 `BaseSkill` 类
2. 实现必要的方法
3. 注册到代理中

### 扩展MCP实现

1. 继承 `BaseMCP` 类
2. 实现必要的方法
3. 配置并使用

## 测试

```bash
pytest tests/
```

## 部署

参考 `deploy/` 目录下的部署配置文件。

## 文档

详细文档请查看 `docs/` 目录。

## 许可证

MIT License
