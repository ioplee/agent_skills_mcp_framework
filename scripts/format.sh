#!/bin/bash

# 代码格式化脚本
echo "Formatting code for Agent-Skill-MCP Framework..."

# 运行Black代码格式化
echo "Running Black code formatting..."
black src/

# 运行isort导入排序
echo "Running isort import sorting..."
isort src/

echo "Code formatting completed successfully!"
