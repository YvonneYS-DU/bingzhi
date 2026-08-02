---
name: loopy-cli
description: Graph Engineer CLI / tool 约定。导入 graph-engineer、HTML 触发等价命令、无 graph repo 临时历史、写图。
status: active
---

# Loopy CLI / Tools（Graph Engineer）

技能：`graph-engineer`。生成和使用 graph 时，通过 CLI 或同名 tool 调用。  
`dashboard/index.html` Graph AI 的操作与下列命令语义对齐。

## 安装约定

```bash
# 项目内入口（后续可做成 python -m loopy / npx loopy）
loopy <command> [args]
```

当前阶段：命令语义先定死；具体实现可以是 shell、Python 或 agent 内 tool。

## 命令一览

| 命令 | 作用 | 场景 |
|------|------|------|
| `loopy graph init` | 在项目生成/刷新 graph 与 dashboard 模板 | 初始化 |
| `loopy graph show` | 打印当前 project_graph 节点 | 调试 |
| `loopy skill import <path>` | 导入 skill → 绑定前后端 + 写入通道 | 场景 1 |
| `loopy skill list` | 已导入 skill | 场景 1 |
| `loopy write` | Cursor/对话消息结构化写入 | 场景 1 |
| `loopy repo analyze <path>` | 分析 repo → 临时版本 | 场景 2 |
| `loopy version list` | 正式 + 临时版本 | 场景 2 |
| `loopy version promote <draft> --as vN` | 临时版本升格 | 场景 2 |

## 场景 1：Skill → 前后端 + Cursor 写入

```bash
loopy skill import .trae/skills/my-skill
# 效果：
# 1. 解析 SKILL.md
# 2. 挂到 graph 节点
# 3. 打开 write 通道
# 4. dashboard 可展示

# Cursor 里用户说「把数据看板标成 doing」
loopy write --type requirement --message "数据看板 doing" --id R04
```

`loopy write` 参数：

```text
--type   preference | requirement | version | project | log
--message  原文或摘要
--id       可选，需求 ID / 版本号
--file     可选，强制写入路径
```

## 场景 2：选 repo → 分析 → 临时版本

```bash
loopy repo analyze /path/to/repo
# 写出：dashboard/VERSIONS/draft-<slug>-<date>.md
# status: temporary

loopy version list --status temporary
loopy version promote draft-foo --as v4
```

## Graph 生成

```bash
loopy graph init [--path .]
```

生成/补齐：

```text
PREFERENCES.md
graph/GRAPH.md（或引用全局 loopy graph）
dashboard/PROJECT.md（若无）
dashboard/REQUIREMENTS.md（若无）
dashboard/VERSIONS/
dashboard/index.html（若无则复制模板）
```

标准节点顺序：

```text
startup:        load_prefs
project_init:   init_dashboard
skill:          skill_import          # 场景 1
ask:            repo_analyze          # 场景 2（问 AI + 选 repo）
pre_change:     understand
post_change:    understand → verify → package → dashboard → record → sync
```

## Agent Tool 映射

| tool 名 | CLI | 说明 |
|---------|-----|------|
| `loopy.graph_init` | `graph init` | 生成 graph |
| `loopy.graph_show` | `graph show` | 查看图 |
| `loopy.skill_import` | `skill import` | 导入 skill |
| `loopy.write` | `write` | 消息落盘 |
| `loopy.repo_analyze` | `repo analyze` | repo → draft |
| `loopy.version_promote` | `version promote` | draft → vN |
| `loopy.version_list` | `version list` | 列版本 |

Agent 在 Cursor 中应优先调 tool；无 tool 时按同等语义直接改 dashboard 文件。

## 退出码

| code | 含义 |
|------|------|
| 0 | 成功 |
| 1 | 参数/路径错误 |
| 2 | 分析或写入失败 |
| 3 | 升格冲突（目标 vN 已存在） |

## 核心原则

```text
CLI/tool 只做具体事：导入、写入、分析、升格。
不在 CLI 里做意图识别。
临时版本默认 temporary，确认后才正式。
```
