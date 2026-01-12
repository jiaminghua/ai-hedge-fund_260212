from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import asyncio

from app.backend.routes import api_router
from app.backend.database.connection import engine
from app.backend.database.models import Base
from app.backend.services.ollama_service import ollama_service

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI 对冲基金 API", description="AI 对冲基金后端 API", version="0.1.0")

# 初始化数据库表（多次运行是安全的）
Base.metadata.create_all(bind=engine)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # 前端 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 包含所有路由
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    """启动事件：检查 Ollama 可用性。"""
    try:
        logger.info("检查 Ollama 可用性...")
        status = await ollama_service.check_ollama_status()
        
        if status["installed"]:
            if status["running"]:
                logger.info(f"✓ Ollama 已安装并运行在 {status['server_url']}")
                if status["available_models"]:
                    logger.info(f"✓ 可用模型：{', '.join(status['available_models'])}")
                else:
                    logger.info("ℹ 当前没有下载任何模型")
            else:
                logger.info("ℹ Ollama 已安装但未运行")
                logger.info("ℹ 您可以从设置页面启动它，或手动运行 'ollama serve'")
        else:
            logger.info("ℹ Ollama 未安装。安装它以使用本地模型。")
            logger.info("ℹ 访问 https://ollama.com 下载并安装 Ollama")
            
    except Exception as e:
        logger.warning(f"无法检查 Ollama 状态：{e}")
        logger.info("ℹ 如果您稍后安装 Ollama，集成将可用")
