---
name: dashboard-node
description: 项目仪表盘节点。改代码后更新项目演进记录——探索、版本、需求追踪。产出 markdown 文件，配合 index.html 给领导看。
node: dashboard
order: 4.5
---

# Dashboard Node — 仪表盘节点

## 干什么

在 package（封装 commit）之后、record（记录日志）之前，更新项目的演进仪表盘。

## 更新顺序

```text
package 完成 → dashboard → record → sync
```

## 需要更新的文件

| 文件 | 什么时候更新 | 更新什么 |
|------|-------------|---------|
| `PROJECT.md` | 项目初始化时创建一次 | 项目边界、技术选型、初始探索 |
| `VERSIONS/v{N}.md` | 每次大改动后；或 draft 升格后 | 做了什么、测试了什么、问题、如何解决（正式） |
| `VERSIONS/draft-*.md` | **不由本节点创建** | 由 `repo_analyze` 写临时版本；本节点只在 promote 后写正式 v{N} |
| `REQUIREMENTS.md` | 新需求进来、旧需求完成；Cursor `loopy.write` | 需求状态、为什么新需求不同于旧需求、未完成项、部署建议 |

## PROJECT.md — 项目概览（初始化时创建）

```text
只在项目启动时写一次。记录：
- 项目是什么、解决什么问题
- 技术边界：用什么、不用什么、为什么
- 初始探索：看了哪些现有方案、为什么选择当前路线
- 第一版代码的边界设计

目的：消除幻觉。让后来的人（包括领导）知道最初是怎么想的。
```

## VERSIONS/v{N}.md — 正式版本记录（每次大改动后追加）

```text
每次完成一个版本/大改动后创建。
文件名：VERSIONS/v1.md, v2.md, v3.md...
状态：formal

内容：
- 这个版本做了什么
- 测试覆盖了什么、结果
- 遇到什么问题、怎么解决的
- 还遗留什么问题
```

## VERSIONS/draft-*.md — 临时版本（repo 分析）

```text
由 repo_analyze 节点生成，不由 dashboard 直接写正式史。
状态：temporary
确认后：loopy version promote → 变成 v{N}.md，再按正式模板补全。
```

## REQUIREMENTS.md — 需求追踪（持续更新）

```text
新需求进来 → 追加一行
旧需求完成 → 标记 done
需求取消 → 标记 cancelled，写原因

关键字段：
- 需求简述
- 哪个版本实现 / 计划哪个版本
- 状态（done / doing / planned / cancelled）
- 和前一个需求的差异（为什么这个需求不是之前的延续）
- 部署建议（上线要注意什么）
```

## Harness 快照归档（切版本时）

切版本（`is_new_version == true`）时，自动归档当前 harness 定义：

```text
graph/harnesses/          →  复制到  .loopy/snapshots/v{N}/
  ├── understand.harness            ├── understand.harness
  ├── verify.harness                ├── verify.harness
  └── ...                           └── ...
```

快照规则：
- 只在切版本时写入，日常更新不触发
- 目录 `.loopy/snapshots/` 对 AI 不可见（除非用户明确指令）
- 用途：对比历史版本验收标准（如 `diff .loopy/snapshots/v1/verify.harness graph/harnesses/verify.harness`）

## 不做的事

- 不发明概念
- 不写"本次改动提升了系统可维护性"之类的空话
- 不让用户填表格——agent 根据实际改动自动写

## 核心规则

```text
写事实，不写评价。
领导看仪表盘是要知道三件事：
1. 项目现在做到哪了
2. 有没有坑
3. 新需求为什么要单独做

切版本时，顺手归档 harness 快照。不额外问，不多余操作。
```
