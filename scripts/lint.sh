#!/bin/bash

# 代码质量检查脚本
echo "Running code quality checks for Agent-Skill-MCP Framework..."

# 运行Black代码格式化检查
echo "Running Black code formatting check..."
black --check src/

# 运行isort导入排序检查
echo "Running isort import sorting check..."
isort --check src/

# 运行flake8代码检查
echo "Running flake8 code check..."
flake8 src/

# 运行mypy类型检查
echo "Running mypy type check..."
mypy src/

echo "Code quality check completed successfully!"
