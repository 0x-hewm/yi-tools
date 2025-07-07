# ---------- 构建阶段 ----------
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# 优化依赖安装，利用缓存
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ---------- 运行阶段 ----------
FROM python:3.12-slim-bookworm

RUN apt-get update \
    && apt-get install -yq --no-install-recommends build-essential git \
    && rm -rf /var/lib/apt/lists/*

# 创建非 root 用户
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

# 拷贝构建产物
COPY --from=builder --chown=$USERNAME:$USERNAME /app /app

WORKDIR /app
USER $USERNAME

# 确保 venv 可用
ENV PATH="/app/.venv/bin:$PATH"

# 启动 FastAPI 服务
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
