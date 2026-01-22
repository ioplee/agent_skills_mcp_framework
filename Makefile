# Agent-Skill-MCP Framework Makefile

# 安装依赖
install:
	pip install -r requirements.txt
	pip install -e .

# 安装开发依赖
install-dev:
	pip install -r requirements.txt
	pip install -e .[dev]

# 运行测试
test:
	pytest

# 运行代码质量检查
lint:
	black --check src/
	isort --check src/
	flake8 src/
	mypy src/

# 格式化代码
format:
	black src/
	isort src/

# 运行示例
run-example:
	python src/examples/example_agent.py

# 构建文档
build-docs:
	cd docs && make html

# 构建Docker镜像
build-docker:
	docker build -t agent-skill-mcp .

# 运行Docker容器
run-docker:
	docker run --env-file .env -v ./logs:/app/logs agent-skill-mcp

# 运行Docker Compose
up:
	docker-compose up -d

# 停止Docker Compose
down:
	docker-compose down

# 清理构建产物
clean:
	rm -rf build dist *.egg-info
	rm -rf docs/build
	rm -rf logs/*
