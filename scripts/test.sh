#!/bin/bash

# 测试脚本
echo "Running tests for Agent-Skill-MCP Framework..."

# 运行单元测试
echo "Running unit tests..."
pytest tests/unit/

# 运行集成测试
echo "Running integration tests..."
pytest tests/integration/

# 运行所有测试
echo "Running all tests..."
pytest

echo "Test completed successfully!"
