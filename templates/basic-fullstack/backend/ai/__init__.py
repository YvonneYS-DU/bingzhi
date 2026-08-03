from .adapter import BaseAIAdapter
from .openai_direct import OpenAIDirectAdapter
from .langchain_llm import LangChainAdapter


def get_adapter() -> BaseAIAdapter:
    """根据环境变量 AI_BACKEND 返回对应的适配器实例。
    
    可选值: openai (默认) | langchain
    """
    import os

    backend = os.getenv("AI_BACKEND", "openai").lower()

    if backend == "langchain":
        return LangChainAdapter()

    return OpenAIDirectAdapter()
