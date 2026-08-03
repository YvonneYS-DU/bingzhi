"""最基础的全栈 AI 聊天服务。

启动:
    cd backend
    pip install -r requirements.txt
    OPENAI_API_KEY=sk-xxx python main.py

切换 AI 后端:
    AI_BACKEND=openai   python main.py   # 直连 OpenAI 兼容 API（默认）
    AI_BACKEND=langchain python main.py   # 通过 LangChain

前端: 打开 templates/basic-fullstack/frontend/index.html 即可
"""

import os
from ai import get_adapter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="AI Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

adapter = get_adapter()


class ChatRequest(BaseModel):
    messages: list[dict]  # [{"role": "user", "content": "..."}, ...]
    stream: bool = False


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "backend": os.getenv("AI_BACKEND", "openai"),
    }


@app.post("/api/chat")
async def chat(req: ChatRequest):
    """同步对话：一次性返回完整回复。"""
    if req.stream:
        async def generate():
            async for token in adapter.stream(req.messages):
                yield token
        return StreamingResponse(generate(), media_type="text/plain")

    reply = await adapter.chat(req.messages)
    return {"reply": reply}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    print(f"AI backend: {os.getenv('AI_BACKEND', 'openai')}")
    print(f"Starting on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
