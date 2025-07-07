# Yi-Tools

基于 FastAPI 的实用工具集。

## 功能特性

- 🚀 基于 FastAPI 的高性能 API
- 🐳 Docker 容器化部署
- 🔧 模块化架构设计
- 📝 自动 API 文档生成
- ⚡ 使用 uv 进行快速包管理

## 快速开始

### 本地运行

```bash
# 克隆项目
git clone https://github.com/0x-hewm/yi-tools.git
cd yi-tools

# 安装 uv（如果未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装依赖
uv sync

# 启动服务
uv run python main.py
```

访问 http://localhost:8000/docs 查看 API 文档

### Docker 运行

```bash
docker pull hewm/yi-tools:latest
docker run -d -p 8000:8000 hewm/yi-tools:latest
```

## API 使用

### 字符串转 Excel

```bash
curl -X POST http://localhost:8000/api/v1/tools/string-to-excel-column \
  -H "Content-Type: application/json" \
  -d '{
    "text": "订单1 订单2 订单3",
    "column_name": "内部订单号", 
    "title": "售后单"
  }' \
  --output result.xlsx
```

## 项目结构

```
src/
├── api/            # API 相关
│   ├── routes/     # 路由处理
│   └── schemas/    # 数据模型
├── core/           # 核心配置
├── services/       # 业务逻辑
└── utils/          # 工具函数
```

## 部署指南

详细部署流程请参考 [DEPLOYMENT.md](./DEPLOYMENT.md)

## 开发

```bash
# 同步开发依赖
uv sync --dev

# 运行测试
uv run pytest

# 代码格式化
uv run black src/

# 添加新依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name
```

## 许可证

MIT License