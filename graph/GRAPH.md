---
name: graph-engineer
description: Graph Engineer 项目级 agent graph。skill 导入、HTML 触发选 repo、临时版本构建历史、改代码前后标准流程。每个节点对应 harness 验收文件。
status: active
---

# Graph Engineer — 项目级 agent 工作图

技能名：**graph-engineer**（`.trae/skills/graph-engineer/SKILL.md`）

## 是什么

```
【bootstrap: 项目启动，harness 落地】
    对任意项目 → .loopy/graph/（nodes + harnesses）+ dashboard + PREFERENCES.md
    ↓
启动时: 读 PREFERENCES.md
    ↓
项目初始化: PROJECT.md + dashboard
    ↓
【Graph AI / HTML 触发】
  SKILL 01 bootstrap · SKILL 02 iterate · SKILL 03 diff
  SKILL 04 选中无 graph 的 repo → 临时版本构建历史 + 写图
    ↓
改代码前：understand
    ↓
改代码后：understand → verify → package → dashboard → record → sync
```

## 不是什么

- 不是意图识别系统
- 不是用户行为分析

**只做固定节点上的具体事。不发明概念，不拖住项目。**

## 核心原则

```text
每个节点只做一件具体的事。先做完，再记录。
能做就不问。要问就问一次，记到 PREFERENCES.md。
无 graph 的 repo 用 temporary 构建历史；确认后再正式 v{N}。
dashboard/index.html 是 AI 一等触发点。
每个节点跑之前知道要什么，跑之后知道对不对。不对就回去重来。
```

## 标准图

```yaml
project_graph:
  name: graph-engineer
  nodes:
    bootstrap:                     # 【新增】对任意项目执行启动，harness 落地
      - bootstrap                  # 落 graph/nodes/ + graph/harnesses/ + dashboard
    startup:
      - load_prefs
    project_init:
      - init_dashboard
    skill:
      - skill_import          # 导入 graph-engineer → 前后端 + 写入
    ask:                        # HTML Graph AI / 对话
      - bootstrap             # SKILL 01
      - iterate               # SKILL 02
      - diff_boss             # SKILL 03
      - repo_analyze          # SKILL 04 无 graph repo → temporary 历史 + 写图
    pre_change:
      - understand
    post_change:
      - understand
      - verify
      - package
      - dashboard             # 只写正式演进；draft 由 repo_analyze 写
      - record
      - sync
```

## 三个产品要点

### 1. 技能叫 Graph Engineer

导入 `.trae/skills/graph-engineer` 后，在 Cursor / Graph AI 里按四个 skill 场景工作。

### 2. 无 graph 的 repo → 临时版本构建历史

```text
选中 folder/repo（可以从未用过 graph）
  → AI 分析
  → 生成版本迭代 draft（temporary）
  → 串成可展示的构建历史
  → 不直接冒充正式发版
```

详见 `nodes/repo_analyze.md`。

### 3. HTML 是 AI 触发点

`dashboard/index.html`：

```text
打开 Graph AI
  → 选 skill / 选 repo folder
  → 提问
  → AI 分析
  → AI 写创建图表 + temporary 时间轴卡片
```

闭环：选 repo → 问 AI → 分析 → 写图。只聊天不算完成。

## 节点说明

| 节点 | 干什么 | harness | 失败策略 |
|------|--------|---------|---------|
| bootstrap | 项目启动，harness 落地到 .loopy/ | [bootstrap.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/bootstrap.harness) | block |
| skill_import | 导入 graph-engineer，展开前后端与写入通道 | [skill_import.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/skill_import.harness) | block |
| repo_analyze | 无 graph repo → draft 历史 + 写图 | [repo_analyze.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/repo_analyze.harness) | warn |
| understand | 改前建基线 / 改后确认改动 | [understand.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/understand.harness) | block |
| verify | 跑测试、lint，只报告不改代码 | [verify.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/verify.harness) | block |
| package | 整理 commit、写 message | [package.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/package.harness) | warn |
| dashboard | 更新演进记录，切版本时归档 harness 快照 | [dashboard.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/dashboard.harness) | warn |
| record | 写入项目日志 | [record.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/record.harness) | warn |
| sync | push 到远端 | [sync.harness](file:///Users/bingzhi/Documents/TRAE/loopy/graph/harnesses/sync.harness) | block |

## Harness 系统

每个节点对应一个 `.harness` 文件，定义输入合约、输出合约、验收规则和失败策略。

- **唯一源：`graph/harnesses/`** — 所有节点只从这里读 harness 定义
- **`.loopy/snapshots/v{N}/`** — 切版本时自动归档的快照。AI 不读，除非用户明确指令
- 详设：**[HARNESS.md](file:///Users/bingzhi/Documents/TRAE/loopy/graph/HARNESS.md)**

## CLI / Tool

见 `cli/LOOPY_CLI.md`。

```bash
loopy skill import graph-engineer
loopy repo analyze <path>
loopy version promote draft-v1 --as v1
loopy write --type requirement --message "..."
```

## 仪表盘

| 文件 | 用途 |
|------|------|
| `index.html` | **触发点** + 可视化图 |
| `VERSIONS/v{N}.md` | 正式版本 |
| `VERSIONS/draft-*.md` | 临时构建历史 |
| `PROJECT.md` / `REQUIREMENTS.md` | 概览与需求 |

## 卡住了

见 `loop/LOOP.md`。
