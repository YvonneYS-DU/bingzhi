---
name: "graph-engineer"
description: "Graph Engineer: bootstrap/iterate architecture graphs, explain version diffs, or select a repo folder to analyze and build temporary version history + graph. Invoke when user opens Graph AI, imports this skill, picks a repo without graph history, or asks to create/update architecture timeline."
---

# Graph Engineer

项目级图工程技能。把「架构图 + 版本演进 + 需求差异」变成 agent 可执行流程。  
配套目录：仓库内 `loopy/`（或本 skill 所在项目的 graph/dashboard）。

## 何时启用

- 用户打开 dashboard `index.html` 的 **Graph AI** 抽屉
- 用户说：建图、迭代图、给领导讲差异、从 repo 反推历史
- 用户**选中一个还没有 graph 的文件夹/repo**，要求分析并生成版本迭代
- Cursor / IDE 里导入本 skill 后发项目消息需要写入 dashboard

## 四个 skill 场景（与 Graph AI UI 对齐）

| ID | UI 名称 | 干什么 |
|----|---------|--------|
| SKILL 01 `bootstrap` | Bootstrap version + create graph | 绿地：定 v1 边界，生成第一张架构图 |
| SKILL 02 `iterate` | Iterate version + update graph | 已有图：加/演进节点，记 delta，不重画整图 |
| SKILL 03 `diff_boss` | What changed / how it differs | 给领导讲清：新工作不是旧需求小补丁 |
| SKILL 04 `repo_history` | Select repo → temporary history | **无 graph 的 repo**：选中 folder，分析，生成**临时版本**构建历史，并写/刷新图表 |

截图里前三个已在 UI；第四个是新增核心能力。

## 场景重点：无 graph 的 repo → 临时版本历史

```text
HTML / 对话里选中 repo folder
    → AI 分析目录、文档、git（若有）
    → 推断合理演进切片（仍标记 temporary）
    → 写入 VERSIONS/draft-*.md（可多份 draft-v1、draft-v2…）
    → AI 写/更新架构图数据（节点、边、每版 nodeChanges）
    → 时间轴展示 temporary 卡片
    → 用户确认后 promote → 正式 v{N}.md
```

### 关键规则

1. **没有使用过 graph 的 repo 也可以用本 skill 补历史**——产出是 temporary，不是直接冒充正式演进。
2. 临时版本文件：`dashboard/VERSIONS/draft-{slug}.md`，frontmatter/抬头含 `状态：temporary`。
3. 可一次生成多条 draft，串成「构建历史」时间线；全部 temporary，直到 `loopy version promote`。
4. **HTML 是 AI 触发点**：选 repo → 提问 → AI 分析 → AI 写创建图表（节点/边/版本卡片）。不要只聊天不落盘、不改图。

### Agent 执行清单（repo_history）

```yaml
repo_history:
  inputs:
    - repo_path: 用户选中的 folder
    - goal: 可选，用户提问
  steps:
    - scan: 结构、栈、README、测试、最近 commit
    - slice: 按可观察事实切 1～N 个演进阶段（宁少勿编）
    - write_drafts: VERSIONS/draft-*.md
    - write_graph: 更新图数据（HTML 内嵌 ARCH 或旁路 graph.json）
    - reply: 说明哪些是推断、哪些是文件事实；提醒 temporary
  never:
    - 把 draft 直接写成正式 v1.md 而不标注 temporary
    - 发明用户没在 repo 里出现的业务愿景
```

## HTML 作为触发点

文件：`dashboard/index.html`

```text
用户打开页面
  → 点 AI / Graph AI
  → 选 skill（含 SKILL 04）
  → 【选中 repo folder】（webkitdirectory / 路径粘贴 / agent 工具传入）
  → 输入问题
  → 发送
  → AI：分析 → 写 draft 版本 → 创建/更新图表 → 时间轴刷新
```

Agent 在 IDE 中被唤起时，等价流程：

1. 读本 `SKILL.md` + `graph/GRAPH.md` + `graph/nodes/repo_analyze.md`
2. 读用户指定 repo
3. 写 `dashboard/VERSIONS/draft-*.md`
4. 更新图（能改 `index.html` 的 ARCH 数据或独立数据文件则改）
5. 用 temporary 状态回复用户

## 与 Cursor 写入

导入本 skill 后，Cursor 消息可写入：

| 类型 | 文件 |
|------|------|
| 偏好 | `PREFERENCES.md` |
| 需求 | `REQUIREMENTS.md` |
| 正式版本 | `VERSIONS/v{N}.md` |
| 临时历史 | `VERSIONS/draft-*.md` |
| 改动日志 | record 节点约定路径 |

## CLI / tool（语义）

见 `cli/LOOPY_CLI.md`：

```bash
loopy skill import graph-engineer
loopy repo analyze <path>          # → temporary drafts + graph seed
loopy version promote <draft> --as vN
loopy write --type ...
```

## 标准 graph 节点

改代码前后仍走：

`understand → verify → package → dashboard → record → sync`

卡壳见 `loop/LOOP.md`。能做就不问；偏好记一次到 `PREFERENCES.md`。

## 输出质量

- 写事实，不写「提升了可维护性」空话
- 领导三问：做到哪了、有没有坑、新需求为何独立
- temporary 必须可丢、可改、可升格
