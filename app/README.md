# Web 应用程序
AI 对冲基金应用是一个完整的系统，包含前端和后端组件，使您能够通过自己计算机上的 Web 界面运行 AI 驱动的对冲基金交易系统。

<img width="1721" alt="Screenshot 2025-06-28 at 6 41 03 PM" src="https://github.com/user-attachments/assets/b95ab696-c9f4-416c-9ad1-51feb1f5374b" />


## 概述

AI 对冲基金由以下部分组成：

- **后端**：一个 FastAPI 应用程序，提供 REST API 来运行对冲基金交易系统和回测器
- **前端**：一个 React/Vite 应用程序，提供用户友好的界面来可视化和控制对冲基金操作

## 目录

- [🚀 快速开始（面向非技术用户）](#-快速开始面向非技术用户)
  - [选项 1：使用 1 行 Shell 脚本（推荐）](#选项-1-使用-1-行-shell-脚本推荐)
  - [选项 2：使用 npm（替代方案）](#选项-2-使用-npm替代方案)
- [🛠️ 手动设置（面向开发者）](#️-手动设置面向开发者)
  - [前提条件](#前提条件)
  - [安装](#安装)
  - [运行应用程序](#运行应用程序)
- [详细文档](#详细文档)
- [免责声明](#免责声明)
- [故障排除](#故障排除])

## 🚀 快速开始（面向非技术用户）

**一行设置和运行命令：**

### 选项 1：使用 1 行 Shell 脚本（推荐）

#### 对于 Mac/Linux：
```bash
./run.sh
```

如果您收到 "permission denied" 错误，请先运行此命令：
```bash
chmod +x run.sh && ./run.sh
```

或者，您也可以运行：
```bash
bash run.sh
```

#### 对于 Windows：
```cmd
run.bat
```

### 选项 2：使用 npm（替代方案）
```bash
cd app && npm install && npm run setup
```

**就这样！** 这些脚本将：
1. 检查所需的依赖项（Node.js、Python、Poetry）
2. 自动安装所有依赖项
3. 启动前端和后端服务
4. **自动打开您的 Web 浏览器** 到应用程序

**要求：**
- [Node.js](https://nodejs.org/)（包含 npm）
- [Python 3](https://python.org/)
- [Poetry](https://python-poetry.org/)

**运行后，您可以访问：**
- 前端（Web 界面）：http://localhost:5173
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

---

## 🛠️ 手动设置（面向开发者）

如果您更喜欢手动设置每个组件或需要更多控制：

### 前提条件

- 前端需要 Node.js 和 npm
- 后端需要 Python 3.8+ 和 Poetry

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
```

2. 设置环境变量：
```bash
# 在根目录创建 .env 文件用于存储 API 密钥
cp .env.example .env
```

3. 编辑 .env 文件以添加您的 API 密钥：
```bash
# 用于运行 openai 托管的 LLM（gpt-4o, gpt-4o-mini 等）
OPENAI_API_KEY=your-openai-api-key

# 用于运行 groq 托管的 LLM（deepseek, llama3 等）
GROQ_API_KEY=your-groq-api-key

# 用于获取为对冲基金提供动力的金融数据
FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key
```

4. 安装 Poetry（如果尚未安装）：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

5. 安装根项目依赖：
```bash
# 从根目录
poetry install
```

6. 安装后端应用依赖：
```bash
# 导航到后端目录
cd app/backend
pip install -r requirements.txt  # 如果存在 requirements.txt 文件
# 或者
poetry install  # 如果后端目录中有 pyproject.toml
```

7. 安装前端应用依赖：
```bash
cd app/frontend
npm install  # 或 pnpm install 或 yarn install
```

### 运行应用程序

1. 启动后端服务器：
```bash
# 在一个终端中，从后端目录
cd app/backend
poetry run uvicorn main:app --reload
```

2. 启动前端应用程序：
```bash
# 在另一个终端中，从前端目录
cd app/frontend
npm run dev
```

现在您可以访问：
- 前端应用程序：http://localhost:5173
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

## 详细文档

如需更详细的信息：
- [后端文档](./backend/README.md)
- [前端文档](./frontend/README.md)

## 免责声明

该项目仅用于**教育和研究目的**。

- 不打算用于实际交易或投资
- 不提供任何保证或担保
- 创建者对财务损失不承担任何责任
- 投资决策请咨询财务顾问

使用本软件，即表示您同意仅将其用于学习目的。

## 故障排除

### 常见问题

#### "Command not found: uvicorn" 错误
如果您在运行设置脚本时看到此错误：

```bash
[ERROR] 后端启动失败。检查日志：
Command not found: uvicorn
```

**解决方案：**
1. **清理 Poetry 环境：**
   ```bash
   cd app/backend
   poetry env remove --all
   poetry install
   ```

2. **或强制重新安装：**
   ```bash
   cd app/backend
   poetry install --sync
   ```

3. **验证安装：**
   ```bash
   cd app/backend
   poetry run python -c "import uvicorn; import fastapi"
   ```

#### Python 版本问题
- **使用 Python 3.11**：Python 3.13+ 可能存在兼容性问题
- **检查您的 Python 版本：** `python --version`
- **根据需要切换 Python 版本**（使用 pyenv、conda 等）

#### 环境变量问题
- **确保 .env 文件存在**于项目根目录
- **从模板复制：** `cp .env.example .env`
- **向 .env 文件添加您的 API 密钥**

#### 权限问题（Mac/Linux）
如果您收到 "permission denied"：
```bash
chmod +x run.sh
./run.sh
```

#### 端口已被占用
如果端口 8000 或 5173 已被占用：
- **终止现有进程：** `pkill -f "uvicorn\|vite"`
- **或使用不同的端口** 通过修改脚本

### 获取帮助
- 查看 [GitHub Issues](https://github.com/virattt/ai-hedge-fund/issues)
- 关注 [Twitter](https://x.com/virattt) 上的更新 
