#!/bin/bash

# 项目初始化脚本
echo "Initializing Agent-Skill-MCP Framework..."

# 创建必要的目录
echo "Creating necessary directories..."
mkdir -p logs

# 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -e .

# 复制环境变量模板
echo "Setting up environment variables..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file from template. Please update it with your configuration."
fi

echo "Initialization completed successfully!"
