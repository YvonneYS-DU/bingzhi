---
name: graph-engine
description: 项目级 agent graph。每个项目有一个专属图，定义改代码前后的标准流程：理解、探索、验证、封装、仪表盘、记录、同步。agent 加载后按图执行。
status: active
---

# Graph Engine — 项目级 agent 工作图

## 是什么

Graph Engine 是项目的 agent 工作流图：

```
启动时: 读 PREFERENCES.md（加载偏好）
    ↓
项目初始化: 创建 PROJECT.md（项目探索、边界、消除幻觉）
    ↓
改代码前：understand（建基线）
    ↓
改代码
    ↓
改代码后：understand → verify → package → dashboard → record → sync
```

## 不是什么

- 不是意图识别系统
- 不是用户行为分析

**Graph 只做一件事：让 agent 改代码前后自动完成标准流程。不发明概念，不拖住项目。**

## 核心原则

```text
每个节点只做一件具体的事。先做完，再记录。
能做就不问。要问就问一次，记到 PREFERENCES.md。
```

## 标准图（默认）

```yaml
project_graph:
  name: "default"
  nodes:
    startup:
      - load_prefs       # 读 PREFERENCES.md

    project_init:
      - init_dashboard   # 创建 PROJECT.md、REQUIREMENTS.md 模板

    pre_change:
      - understand       # 改前理解：记录当前状态

    post_change:
      - understand       # 改后理解：确认改了什么、影响范围
      - verify           # 验证：跑测试、lint
      - package          # 封装：整理 commit
      - dashboard        # 仪表盘：更新项目演进记录
      - record           # 记录：写改动日志
      - sync             # 同步：push
```

## 节点说明

| 节点 | 干什么 | 输入 | 输出 |
|------|--------|------|------|
| load_prefs | 加载用户偏好 | PREFERENCES.md | 行为规则 |
| init_dashboard | 初始化项目仪表盘 | 项目信息 | PROJECT.md, REQUIREMENTS.md |
| understand | 读懂代码改动 | diff、文件列表 | 改动说明、影响范围 |
| verify | 确认改动正确 | 改动说明 | 测试结果、lint 结果 |
| package | 整理提交 | 所有改动 | commit message、staged files |
| dashboard | 更新项目演进 | 改动、测试结果 | PROJECT.md, VERSIONS/v{N}.md, REQUIREMENTS.md |
| record | 记录改动原因 | commit 信息 | 项目日志条目 |
| sync | 推送到远端 | commit | push 结果 |

## 仪表盘系统

`dashboard/` 目录包含项目演进仪表盘：

| 文件 | 用途 | 什么时候更新 |
|------|------|-------------|
| `PROJECT.md` | 项目概览、技术边界、初始探索 | 项目初始化 |
| `VERSIONS/v{N}.md` | 版本记录 | 每次大改动后 |
| `REQUIREMENTS.md` | 需求追踪 | 新需求进入/完成 |
| `index.html` | 可视化仪表盘 | 静态，直接给领导看 |

使用方法：在 dashboard/ 目录下运行 `python3 -m http.server 8080`，浏览器打开 `http://localhost:8080`。

## 自定义图

项目可以增减节点。详见各个节点文档。

## 图卡住了怎么办

详见 `loop/LOOP.md`。
