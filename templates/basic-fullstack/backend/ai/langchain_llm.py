"""LangChain 集成。

通过 LangChain 调用 LLM，方便后续扩展（Chain / Agent / Tool 等）。

环境变量:
    OPENAI_API_KEY      API 密钥
    OPENAI_BASE_URL     接口地址（可选）
    OPENAI_MODEL        模型名（可选，默认 gpt-4o-mini）
"""

import os
from typing import AsyncIterator

from .adapter import BaseAIAdapter


class LangChainAdapter(BaseAIAdapter):

    def __init__(self):
        # 延迟导入，避免未安装 langchain 时启动报错
        from langchain_openai import ChatOpenAI

        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY", "sk-xxx"),
            base_url=os.getenv("OPENAI_BASE_URL", None),
            temperature=0.7,
            max_tokens=2048,
        )

    async def chat(self, messages: list[dict], **kwargs) -> str:
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

        role_map = {
            "system": SystemMessage,
            "user": HumanMessage,
            "assistant": AIMessage,
        }
        lc_messages = [
            role_map[m["role"]](m["content"])
            for m in messages
            if m["role"] in role_map
        ]

        resp = await self.llm.ainvoke(lc_messages)
        return resp.content

    async def stream(self, messages: list[dict], **kwargs) -> AsyncIterator[str]:
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

        role_map = {
            "system": SystemMessage,
            "user": HumanMessage,
            "assistant": AIMessage,
        }
        lc_messages = [
            role_map[m["role"]](m["content"])
            for m in messages
            if m["role"] in role_map
        ]

        async for chunk in self.llm.astream(lc_messages):
            if chunk.content:
                yield chunk.content
