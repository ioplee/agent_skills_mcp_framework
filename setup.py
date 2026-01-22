from setuptools import setup, find_packages

setup(
    name="agent-skill-mcp-framework",
    version="1.0.0",
    description="企业级大模型开发框架基于agent-skill-mcp架构",
    long_description=open("README.md", "r", encoding="utf-8").read() if open("README.md", "r", encoding="utf-8").read() else "企业级大模型开发框架",
    long_description_content_type="text/markdown",
    author="Your Team",
    author_email="your-email@example.com",
    url="https://github.com/your-org/agent-skill-mcp-framework",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "python-dotenv>=1.0.0",
        "loguru>=0.7.0",
        "aiosignal>=1.3.1",
        "async-timeout>=4.0.3"
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.11.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.7.0"
        ],
        "docs": [
            "sphinx>=7.2.0",
            "sphinx-rtd-theme>=1.3.0"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "agent-skill-mcp=agent_skill_mcp.cli:main"
        ]
    }
)
