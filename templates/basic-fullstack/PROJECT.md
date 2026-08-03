# 基础前后端 AI 聊天模板

> 最简全栈模板：前端聊天 UI + 后端 FastAPI + 可替换 AI 适配器。

## 项目是什么

一个可以直接启动的最基础前后端应用。员工通过 Web 聊天界面与 AI 对话，后端支持两种 AI 接入方式：
- **OpenAI 直连**：通过 `httpx` 直接调用 OpenAI 兼容 API
- **LangChain**：通过 LangChain 的 `ChatOpenAI` 调用，方便后续扩展 Chain / Agent

## 技术栈

| 层 | 选型 | 原因 |
|----|------|------|
| 前端 | HTML + CSS + Vanilla JS | 零依赖，打开即用 |
| 后端 | Python FastAPI | 异步支持好，适合流式输出 |
| AI 层 | adapter 模式 | 通过 `AI_BACKEND` 环境变量切换，新增 AI 后端只需继承 `BaseAIAdapter` |

## 架构图

```
[用户] → 前端 (index.html) → FastAPI → AI Adapter
                                          ├── OpenAI 直连 → OpenAI 兼容 API
                                          └── LangChain    → LangChain ChatOpenAI
```

## 启动

```bash
# 1. 后端
cd backend
cp .env.example .env   # 填入 OPENAI_API_KEY
pip install -r requirements.txt
python main.py          # 默认 http://localhost:8000

# 切换 AI 后端
AI_BACKEND=langchain python main.py

# 2. 前端
# 直接用浏览器打开 frontend/index.html
# 或
cd frontend && python3 -m http.server 3000
```

## AI 适配器接口

所有 AI 后端统一通过 `BaseAIAdapter` 接口访问：

```python
class BaseAIAdapter(ABC):
    async def chat(self, messages: list[dict]) -> str: ...
    async def stream(self, messages: list[dict]) -> AsyncIterator[str]: ...
```

新增 AI 后端只需 3 步：
1. 继承 `BaseAIAdapter`，实现 `chat()` 和 `stream()`
2. 在 `ai/__init__.py` 的 `get_adapter()` 中注册新的 backend 名称
3. 通过 `AI_BACKEND=xxx` 切换

## 为什么选择这个模板

- **零额外依赖的前端**：HTML 直接打开，不需要 Node.js / npm
- **AI 层可插拔**：直连 API 和 LangChain 共用同一套接口，方便教学对比
- **流式输出**：支持 SSE streaming，前端实时显示 AI 回复
- **易于扩展**：后续可以加 Chain、Agent、Tool calling 等 LangChain 高级功能
