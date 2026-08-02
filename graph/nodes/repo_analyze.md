---
name: repo-analyze-node
description: 从 Graph AI / 问 AI 处选中文件夹 repo。无 graph 的仓库可分析并生成临时版本迭代，用来构建历史；并触发写图。
node: repo_analyze
order: 0.5
---

# Repo Analyze Node — 仓库分析 / 构建历史

## 干什么

**给还没有使用 graph 的 repo 补演进史。**

在 Graph AI（`dashboard/index.html`）或对话里选中 folder/repo → AI 分析 → 按 repo 生成**版本迭代（temporary）** → 串成可展示的构建历史 → AI 写创建/更新架构图。

```text
选中 folder / repo（可无任何 loopy/graph 历史）
    ↓
AI 分析（结构、边界、现状、可观察演进）
    ↓
生成 临时版本 draft（可多条，构成历史）
    ↓
AI 写图表（节点、边、每版 nodeChanges）
    ↓
用户确认 → promote 为正式 v{N}
```

## 为什么需要

| 情况 | 做法 |
|------|------|
| 绿地新项目 | 用 SKILL 01 bootstrap |
| 已有 graph，继续迭代 | 用 SKILL 02 iterate |
| **老 repo，从没建过 graph** | **用本节点 / SKILL 04：临时版本构建历史** |
| 给领导讲差异 | SKILL 03 |

临时版本 = 可讨论的历史草稿，**不是**已经发生的正式发版记录。

## 入口（HTML 是主触发点）

| 入口 | 说明 |
|------|------|
| `dashboard/index.html` Graph AI | 选 SKILL 04 → 选 repo folder → 提问 → 发送 |
| 对话 @folder | 用户附带目录 |
| CLI | `loopy repo analyze <path>` |
| tool | `loopy.repo_analyze` |

HTML 流程必须闭环：

```text
选中 repo → 问 AI → AI 分析 → AI 写创建图表 + draft 文件
```

只聊天、不改图、不写 draft = 未完成节点。

## 分析做什么

```yaml
repo_analyze:
  scan:
    - 目录结构、主要语言与框架
    - README / 已有文档
    - 最近 commit（若有 git）
    - 测试与部署线索
  synthesize:
    - 项目是什么、边界在哪
    - 能否从代码/文档切片出 1～N 个演进阶段
    - 每阶段建议节点与关系（用于画图）
  emit:
    - VERSIONS/draft-*.md（status: temporary）
    - 图数据更新（ARCH / graph 数据）
    - 可选 PROJECT.md 草稿段
```

只写事实和可验证观察。阶段切不动就少切，禁止编造业务故事。

## 临时版本（构建历史）

正式：`VERSIONS/v1.md`…  
临时：`VERSIONS/draft-v1.md`、`draft-v2.md` 或 `draft-{slug}-{date}.md`

| | 正式 v{N} | 临时 draft（构建历史） |
|--|-----------|------------------------|
| 来源 | 真实大改动 / promote | 对无 graph repo 的分析 |
| 时间轴 | 主轴 | 带 TEMP 标记 |
| 进领导结论 | 可以 | 否，需确认 |
| 图表 | 正式 nodeChanges | AI 写入的建议图，可改 |

### 多 draft 串历史

无 graph 的 repo 一次分析可以产出：

```text
draft-v1  基线：主链路跑通
draft-v2  推断的下一阶段（仅当 repo 有证据）
…
```

全部 `temporary`。用户可删、可改顺序、可只 promote 其中一条。

## 与 graph-engineer skill

本节点 = Graph Engineer 的 **SKILL 04**。  
完整技能说明：`.trae/skills/graph-engineer/SKILL.md`。

## CLI / Tool

```bash
loopy repo analyze ./legacy-app
# → draft-*.md + 图种子

loopy version list --status temporary
loopy version promote draft-v1 --as v1
```

| tool | 作用 |
|------|------|
| `loopy.repo_analyze` | path → drafts + graph |
| `loopy.version_promote` | draft → 正式 v{N} |
| `loopy.version_list` | formal / temporary |

## 不做的事

- 不把分析草稿直接当正式发版史
- 不在分析阶段强制跑完 verify/package/sync
- 不为了「好看」硬凑 5 个版本

## 核心规则

```text
无 graph 的 repo → 选中 folder → 临时版本构建历史 → AI 写图。
临时可丢；确认后才正式。
HTML Graph AI 是一等触发点，不是装饰。
```
