"""直连 OpenAI 兼容 API。

支持任何兼容 OpenAI 接口的服务（OpenAI / Azure / 本地模型等），
通过环境变量配置:

    OPENAI_API_KEY      API 密钥（必填）
    OPENAI_BASE_URL     接口地址（可选，默认 https://api.openai.com/v1）
    OPENAI_MODEL        模型名（可选，默认 gpt-4o-mini）
"""

import os
from typing import AsyncIterator

import httpx

from .adapter import BaseAIAdapter


class OpenAIDirectAdapter(BaseAIAdapter):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "sk-xxx")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def _url(self) -> str:
        return f"{self.base_url.rstrip('/')}/chat/completions"

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(self, messages: list[dict], **kwargs) -> str:
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 2048),
        }

        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(self._url(), json=payload, headers=self._headers())
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"]["content"]

    async def stream(self, messages: list[dict], **kwargs) -> AsyncIterator[str]:
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 2048),
            "stream": True,
        }

        async with httpx.AsyncClient(timeout=120) as client:
            async with client.stream(
                "POST", self._url(), json=payload, headers=self._headers()
            ) as resp:
                resp.raise_for_status()
                async for line in resp.aiter_lines():
                    if line.startswith("data: ") and line != "data: [DONE]":
                        import json
                        chunk = json.loads(line[len("data: "):])
                        delta = chunk["choices"][0].get("delta", {})
                        if "content" in delta:
                            yield delta["content"]
