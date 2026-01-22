#!/bin/bash

# 版本发布脚本
echo "Releasing Agent-Skill-MCP Framework..."

# 检查版本参数
if [ -z "$1" ]; then
    echo "Usage: ./release.sh <version>"
    exit 1
fi

VERSION=$1

# 运行构建脚本
echo "Building project..."
bash scripts/build.sh

# 更新版本号
echo "Updating version to $VERSION..."
sed -i "s/version=\"[0-9]*\.[0-9]*\.[0-9]*\"/version=\"$VERSION\"/g" setup.py

# 构建包
echo "Building package..."
python setup.py sdist bdist_wheel

echo "Release $VERSION prepared successfully!"
echo "You can now upload the package to PyPI using: twine upload dist/*"
