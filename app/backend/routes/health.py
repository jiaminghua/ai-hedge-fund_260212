from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import asyncio
import json

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "欢迎使用 AI 对冲基金 API"}


@router.get("/ping")
async def ping():
    async def event_generator():
        for i in range(5):
            # 为每个 ping 创建一个 JSON 对象
            data = {"ping": f"心跳 {i+1}/5", "timestamp": i + 1}

            # 格式化为 SSE
            yield f"data: {json.dumps(data)}\n\n"

            # 等待 1 秒
            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")
