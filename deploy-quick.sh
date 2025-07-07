#!/bin/bash

# Yi-Tools 快速部署脚本

set -e

echo "🚀 Yi-Tools 部署工具"
echo "===================="

# 函数：本地测试
test_local() {
    echo "📋 开始本地测试..."
    docker build -t yi-tools:test .
    docker run -d -p 8000:8000 --name test yi-tools:test
    
    echo "⏳ 等待服务启动..."
    sleep 5
    
    if curl -f http://localhost:8000/api/v1/health/ > /dev/null 2>&1; then
        echo "✅ 本地测试通过"
        docker stop test && docker rm test
        return 0
    else
        echo "❌ 本地测试失败"
        docker logs test
        docker stop test && docker rm test
        return 1
    fi
}

# 函数：构建并推送
build_push() {
    echo "🔨 构建并推送镜像..."
    
    # 确保 buildx 可用
    docker buildx inspect multiarch > /dev/null 2>&1 || docker buildx create --name multiarch --use
    
    # 构建并推送
    docker buildx build \
        --platform linux/amd64,linux/arm64 \
        -t hewm/yi-tools:latest \
        -t hewm/yi-tools:$(date +%Y%m%d-%H%M) \
        --push .
    
    echo "✅ 镜像推送完成"
}

# 函数：服务器部署
deploy_server() {
    echo "🚀 准备服务器部署命令..."
    echo ""
    echo "请在服务器上执行以下命令："
    echo "================================="
    echo "cd /opt/yi-tools"
    echo "docker-compose pull"
    echo "docker-compose down"
    echo "docker-compose up -d"
    echo "docker-compose logs -f yi-tools"
    echo "================================="
}

# 主程序
case "${1:-help}" in
    "test")
        test_local
        ;;
    "deploy")
        test_local && build_push && deploy_server
        ;;
    "build")
        build_push
        ;;
    *)
        echo "用法: $0 {test|build|deploy}"
        echo "  test   - 本地测试"
        echo "  build  - 构建推送镜像"
        echo "  deploy - 完整部署流程"
        exit 1
        ;;
esac
