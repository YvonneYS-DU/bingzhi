# LangChain 考试白名单复习指南

> 这份文档是给你考前复习用的，不是考试中可打开的资料。
> 考试时只允许使用白名单站点：
> `smith.langchain.com`、`docs.langchain.com`、`academy.langchain.com`

## 1. 这场考试本质在考什么

`LangChain Certified Agent Engineer` 不是单纯背 API 的考试，更像是：

- 概念判断题
- 场景选择题
- 产品边界题
- LangSmith 界面阅读题

官方 4 大模块：

- `Build`: 怎么构建 agent
- `Test`: 怎么评测 agent
- `Deploy`: 怎么部署 agent
- `Monitor`: 怎么观察和告警

核心复习主线：

```text
Build -> Test -> Deploy -> Monitor
```

你做题时通常要判断：

- 这个问题属于哪一层
- 该用哪个产品能力
- 该看哪个界面
- 该用哪类 evaluator / trace / deployment 概念

---

## 2. 白名单长什么样

考试允许访问的只有 3 个站：

### `academy.langchain.com`

作用：

- 看课程
- 看认证页
- 看考试说明

你最关心的页面类型：

- 认证页
- 前置课程页
- 课程章节页

它更像：

- 学习入口
- 官方课程目录
- 考纲来源

适合查：

- 这门认证考哪几块
- 官方推荐先学哪些课程
- 对某个模块的大致范围做最后确认

不适合查：

- 细节 API
- 代码参数对比
- LangSmith 实操字段解释

### `docs.langchain.com`

作用：

- 官方文档主站
- 代码/API/概念说明
- LangChain / Deep Agents / LangGraph / LangSmith 文档都在这里

你可以把它理解成：

- 考试里的官方检索站
- 最重要的白名单资料站

最重要的几个入口：

- `docs.langchain.com/oss/python/langchain/overview`
- `docs.langchain.com/oss/python/deepagents/overview`
- `docs.langchain.com/langsmith/home`
- `docs.langchain.com/langsmith/evaluation`
- `docs.langchain.com/langsmith/deployment`
- `docs.langchain.com/langsmith/observability`

它更像：

- 目录页 + 概念页 + quickstart

考试里如果你脑子空白，通常先回到这些 overview 页面，再往下点二级页。

### `smith.langchain.com`

作用：

- LangSmith 实际产品界面
- 查看 traces
- 看 datasets / experiments
- 看 online eval
- 看 deployment / assistant / thread / run

它更像：

- 操作台
- 证据现场

考试里官方会给你一个专用的 `LangSmith organization`，有些题就是要你进这个界面看内容再选答案。

你可以把它理解为：

- 考试专用工作区
- 放 trace / dataset / run / experiment 的地方
- 一部分题目的题干材料来源

---

## 3. 考试时最值得先记住的查找路线

如果做题时忘了概念，优先按这个路线找：

### Build 题

先看：

- `docs.langchain.com/oss/python/langchain/overview`
- `docs.langchain.com/oss/python/deepagents/overview`

重点找这些词：

- `create_agent`
- `middleware`
- `deepagents`
- `skills`
- `memory`
- `context`
- `filesystem`
- `sandbox`

### Test 题

先看：

- `docs.langchain.com/langsmith/evaluation`

重点找这些词：

- `dataset`
- `example`
- `evaluator`
- `experiment`
- `offline evaluation`
- `online evaluation`
- `LLM-as-judge`
- `pairwise`

### Deploy 题

先看：

- `docs.langchain.com/langsmith/deployment`

重点找这些词：

- `deployment`
- `assistant`
- `thread`
- `run`
- `revision`
- `Agent Server`
- `cloud`
- `hybrid`
- `self-hosted`

### Monitor 题

先看：

- `docs.langchain.com/langsmith/observability`

重点找这些词：

- `trace`
- `debug`
- `dashboards`
- `alerts`
- `online evaluations`
- `feedback`
- `threads`

---

## 4. 你大概会看到哪些概念

### Build

#### `create_agent`

用途：

- LangChain 里创建 agent 的最常见入口
- 属于一个相对轻量、可组合的 agent harness

适合什么题：

- 想要一个可定制 agent
- 用 model + tools + prompt + middleware 组装 agent

一句话记忆：

`create_agent = 标准、轻量、可组合的 agent 入口`

#### `deepagents`

用途：

- 适合更复杂、更长流程的 agent
- 支持更强的上下文管理、子代理、文件系统、任务规划

官方 overview 里提到的关键能力方向：

- plan
- subagents
- virtual filesystem
- context management
- skills
- memory
- summarization / context offloading

一句话记忆：

`deepagents = 更重型、更适合复杂长任务的 agent harness`

#### `middleware`

用途：

- 在 agent 执行链路中插入控制逻辑
- 用来做 guardrails、策略、路由、重试、工具控制

一句话记忆：

`middleware = 在 agent 外围加行为控制层`

#### `context engineering`

用途：

- 让 agent 在运行过程中看到合适的信息
- 管理哪些信息进入上下文、哪些被压缩、哪些被长期保留

一句话记忆：

`context engineering = 管理 agent 在每一步看到什么`

### Test

#### `dataset`

用途：

- 一组测试样本

一句话记忆：

`dataset = 测试题库`

#### `example`

用途：

- dataset 里的一条样本

一句话记忆：

`example = 一道具体测试样本`

#### `evaluator`

用途：

- 评分器
- 判断结果好坏

常见类型：

- `code evaluator`
- `human review`
- `LLM-as-judge`
- `pairwise`

一句话记忆：

`evaluator = 评分标准`

#### `experiment`

用途：

- 在 dataset 上跑一轮应用，得到的评测结果集合

一句话记忆：

`experiment = 某版本在某批测试集上的测评记录`

#### `offline evaluation`

用途：

- 开发期离线测
- 用于对比版本、回归测试、基准测试

一句话记忆：

`offline = 上线前评测`

#### `online evaluation`

用途：

- 生产环境实时评测
- 在真实流量上自动跑评估

一句话记忆：

`online = 线上真实流量监控`

### Deploy

#### `deployment`

用途：

- 把 agent 变成可运行、可服务的生产环境实例

一句话记忆：

`deployment = 已经可以跑起来提供服务的版本`

#### `assistant`

用途：

- Agent Server 里的交互配置实体

一句话记忆：

`assistant = 面向交互的 agent 配置实体`

#### `thread`

用途：

- 一条会话或任务上下文

一句话记忆：

`thread = 上下文线`

#### `run`

用途：

- 一次具体执行

一句话记忆：

`run = 某次实际运行`

#### `revision`

用途：

- 某次部署版本或变更后的版本

一句话记忆：

`revision = 部署版本号/修订版`

### Monitor

#### `trace`

用途：

- 一次执行的细节链路
- 看每一步做了什么、调用了什么、哪里慢、哪里错

一句话记忆：

`trace = 运行过程录像`

#### `dashboard / alerts / feedback`

用途：

- dashboard 看趋势
- alerts 看异常
- feedback 看人工或用户反馈

一句话记忆：

`monitor = 看趋势、看异常、看反馈`

---

## 5. 最小 API 心智模型

你不用记住一堆散乱 API，先记住下面这套最小模型。

```text
LangChain:
model + tools + prompt + middleware -> create_agent -> invoke

LangSmith Test:
dataset + evaluators -> experiment -> compare results

LangSmith Monitor:
runs -> traces -> dashboards / alerts / feedback

LangSmith Deploy:
graph/app -> deployment -> assistant -> thread -> run
```

---

## 6. 最小代码样例

以下是考前帮助你理解结构的，不代表考试一定要求手写代码。

### 6.1 `create_agent` 最小样例

```python
from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "What's the weather in San Francisco?"}
        ]
    }
)

print(result["messages"][-1].content_blocks)
```

这段代码你至少要能看懂：

- `model` 是模型
- `tools` 是工具
- `system_prompt` 是系统提示词
- `invoke()` 是执行入口

### 6.2 LangSmith tracing 最小理解

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=your_api_key
```

理解重点：

- 打开 tracing 后，运行就会进 LangSmith
- 然后你能在 `smith.langchain.com` 里看 traces

### 6.3 Evaluation 的最小流程

```text
1. 创建 dataset
2. 往 dataset 里放 examples
3. 定义 evaluator
4. 在 dataset 上跑 experiment
5. 对比结果
```

你不用执着于每个 SDK 函数名，考试更可能考你：

- 先做哪一步
- 哪种 evaluator 更合适
- 结果应该怎么看

### 6.4 Deployment 的最小理解

```text
本地 agent / graph
-> 部署到 LangSmith Deployment
-> 生成可服务的 deployment
-> 通过 assistant / thread / run 与它交互
```

### 6.5 Monitor 的最小理解

```text
一次请求
-> 生成 run
-> 可以看到 trace
-> 聚合到 dashboard
-> 配合 online evaluations / alerts 持续监控
```

---

## 7. 白名单里真正值得看的页面

下面这些页面最值得提前熟悉，因为考试中如果要查，通常就从这些入口开始。

### 文档总入口

- `https://docs.langchain.com/oss/python/langchain/overview`
- `https://docs.langchain.com/oss/python/deepagents/overview`
- `https://docs.langchain.com/langsmith/home`
- `https://docs.langchain.com/langsmith/evaluation`
- `https://docs.langchain.com/langsmith/deployment`
- `https://docs.langchain.com/langsmith/observability`

### 课程与考试入口

- `https://academy.langchain.com/pages/certifications-lcae`

### 真实产品入口

- `https://smith.langchain.com/`

---

## 8. 你进入白名单后应该怎么读

因为官方文档不算好读，建议按下面方式看。

### 先看 overview，不要一开始钻 reference

先看：

- overview
- quickstart
- concepts

不要一上来就看：

- 细碎 reference
- 很深的 provider 参数页

原因：

- 认证更偏概念边界和场景判断
- 不太像让你背一堆底层参数

### 遇到陌生词先问 3 个问题

- 这是 `Build / Test / Deploy / Monitor` 里的哪一类
- 它是一个对象、流程、还是评分方式
- 它和相邻概念的区别是什么

例如：

- `thread` 和 `run` 的区别
- `offline eval` 和 `online eval` 的区别
- `create_agent` 和 `deepagents` 的区别

### 优先找图和流程

如果一个页面有：

- workflow
- quickstart
- concepts
- comparison

优先看这些区域。

---

## 9. 高频对比题速记

### `create_agent` vs `deepagents`

- `create_agent`: 标准轻量、灵活拼装
- `deepagents`: 更复杂、更长流程、更多上下文与代理能力

### `offline evaluation` vs `online evaluation`

- `offline`: 上线前，在 dataset 上测
- `online`: 上线后，在真实流量上测

### `dataset` vs `example`

- `dataset`: 样本集合
- `example`: 单条样本

### `assistant` vs `thread` vs `run`

- `assistant`: agent 配置实体
- `thread`: 一条上下文线
- `run`: 一次执行

### `trace` vs `dashboard`

- `trace`: 单次执行明细
- `dashboard`: 多次执行聚合观察

---

## 10. 考试前建议准备什么

### 你可以提前准备

- 自己的笔记
- 自己的 `md`
- 自己的脑图
- 课程摘要
- 高频对比表

### 但考试时不能打开

- 本地 `md`
- `Word`
- `Notion`
- 飞书文档
- 自己做的 PDF
- 非白名单网页

所以正确做法是：

- 现在用这份文档复习
- 考前把这些知识压缩进脑子
- 考试时只在白名单站点里定位官方内容

---

## 11. 你考前最少要熟到什么程度

理想目标不是会默写所有 API，而是达到下面程度：

- 看到题目能判断它属于哪一模块
- 能说出该去哪一个白名单站点找
- 能区分高频概念对
- 能看懂 LangSmith 界面里的基本对象
- 能读懂 `create_agent` 这类最小示例

如果你能做到这些，这场选择题就不是“乱猜”，而是“带着结构去选”。

---

## 12. 最后一页速记

```text
Build:
create_agent / deepagents / middleware / context / skills / memory

Test:
dataset / example / evaluator / experiment / offline / online

Deploy:
deployment / assistant / thread / run / revision / Agent Server

Monitor:
trace / dashboards / alerts / feedback / online evals

白名单:
academy.langchain.com
docs.langchain.com
smith.langchain.com
```
