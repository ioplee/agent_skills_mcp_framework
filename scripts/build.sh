#!/bin/bash

# 构建脚本
echo "Building Agent-Skill-MCP Framework..."

# 运行代码质量检查
echo "Running code quality checks..."
bash scripts/lint.sh

# 运行测试
echo "Running tests..."
bash scripts/test.sh

# 构建包
echo "Building package..."
python setup.py sdist bdist_wheel

echo "Build completed successfully!"
