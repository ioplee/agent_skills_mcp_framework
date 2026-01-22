#!/bin/bash

# 清理脚本
echo "Cleaning up Agent-Skill-MCP Framework..."

# 清理构建产物
echo "Removing build artifacts..."
rm -rf build dist *.egg-info

# 清理文档构建产物
echo "Removing documentation build artifacts..."
rm -rf docs/build

# 清理日志文件
echo "Removing log files..."
rm -rf logs/*

# 清理临时文件
echo "Removing temporary files..."
find . -name "*.pyc" -type f -delete
find . -name "__pycache__" -type d -delete

# 清理Docker相关文件
echo "Removing Docker related files..."
docker system prune -f

echo "Cleanup completed successfully!"
