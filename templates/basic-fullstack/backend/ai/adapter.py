"""AI 适配器统一接口。

新增 AI 后端时只需:
1. 继承 BaseAIAdapter
2. 实现 chat() 和 stream()
3. 在 ai/__init__.py 的 get_adapter() 中注册
"""

from abc import ABC, abstractmethod
from typing import AsyncIterator


class BaseAIAdapter(ABC):
    """所有 AI 后端的抽象基类。"""

    @abstractmethod
    async def chat(self, messages: list[dict], **kwargs) -> str:
        """同步对话：传入完整消息列表，返回一次完整回复。"""
        ...

    @abstractmethod
    async def stream(self, messages: list[dict], **kwargs) -> AsyncIterator[str]:
        """流式对话：逐 token yield 回复片段。"""
        ...
