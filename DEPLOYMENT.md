# Yi-Tools 部署流程

## 项目简介

基于 FastAPI 的工具集项目。

## 开发环境设置

### 本地开发

```bash
# 1. 克隆项目
git clone https://github.com/0x-hewm/yi-tools.git
cd yi-tools

# 2. 安装 uv（如果未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. 同步依赖
uv sync

# 4. 本地运行
uv run python main.py
```

### Docker 本地测试

```bash
# 构建镜像
docker build -t yi-tools:test .

# 运行容器
docker run -d -p 8000:8000 --name yi-tools-test yi-tools:test

# 测试 API
curl http://localhost:8000/
curl http://localhost:8000/api/v1/health/

# 测试主要功能
curl -X POST http://localhost:8000/api/v1/tools/string-to-excel-column \
  -H "Content-Type: application/json" \
  -d '{"text": "测试 数据 处理", "column_name": "订单号", "title": "测试导出"}' \
  --output test.xlsx

# 清理测试容器
docker stop yi-tools-test && docker rm yi-tools-test
```

## 代码更新后的完整流程

### 1. 本地测试

```bash
# 代码修改后
git add .
git commit -m "feat: 添加新功能"

# 本地 Docker 测试
docker build -t yi-tools:test .
docker run -d -p 8000:8000 --name test yi-tools:test

# 验证功能正常后清理
docker stop test && docker rm test && docker rmi yi-tools:test
```

### 2. 推送代码到 GitHub

```bash
git push origin main
```

### 3. 构建并上传到 Docker Hub

```bash
# 创建多架构构建器（首次运行）
docker buildx create --name multiarch --use

# 构建并推送多架构镜像
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t hewm/yi-tools:latest \
  -t hewm/yi-tools:v$(date +%Y%m%d-%H%M) \
  --push .

# 验证镜像
docker buildx imagetools inspect hewm/yi-tools:latest
```

### 4. 服务器部署

#### 拉取最新镜像

docker-compose pull

#### 重启服务

docker-compose down
docker-compose up -d

#### 查看运行状态

docker-compose ps
docker-compose logs -f yi-tools

#### 验证服务

```shell
curl <http://localhost:8000/api/v1/health/>

```

## 快速命令参考

### 开发

```bash
# 本地运行
uv run python main.py

# Docker 本地测试
docker build -t test . && docker run -p 8000:8000 test
```

### 部署

```bash
# 一键构建推送
docker buildx build --platform linux/amd64,linux/arm64 -t hewm/yi-tools:latest --push .

# 服务器一键更新
docker-compose pull && docker-compose up -d
```

### 监控

```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f yi-tools

# 查看资源使用
docker stats yi-tools
```

## 环境变量配置

### 生产环境

在服务器上创建 `.env` 文件：

```bash
# 应用配置
DEBUG=false
HOST=0.0.0.0
PORT=8000

# 日志级别
LOG_LEVEL=info
```

## 故障排除

### 常见问题

1. **架构不匹配**：确保使用 `--platform linux/amd64,linux/arm64`
2. **端口冲突**：检查 8000 端口是否被占用
3. **权限问题**：确保 logs 目录权限正确

### 检查命令

```bash
# 检查容器状态
docker-compose ps

# 查看详细日志
docker-compose logs --tail=100 yi-tools

# 进入容器调试
docker-compose exec yi-tools /bin/bash
```
