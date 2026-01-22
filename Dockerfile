FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -e .

# 创建日志目录
RUN mkdir -p logs

# 设置环境变量
ENV LOG_LEVEL=INFO
ENV LOG_FILE=logs/app.log
ENV AGENT_NAME=DockerAgent
ENV AGENT_TIMEOUT=30

# 运行示例
CMD ["python", "src/examples/example_agent.py"]
