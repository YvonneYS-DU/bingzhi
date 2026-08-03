---
name: bootstrap-node
description: 项目启动节点。对任意项目执行初始化，将 harness 体系、dashboard 模板、graph 定义全部落入项目目录。完成后 AI 可直接开始项目的部署与实践。
node: bootstrap
order: -1
on_failure: block
---

# Bootstrap Node — 项目启动 / Harness 落地

## 干什么

对**任意项目**执行启动初始化。这是 loopy 进入项目的第一步：把整套 graph + harness + dashboard 体系落到项目里，让 AI 有完整的可验收工作流可以直接开始部署与实践。

```text
选中项目（任意目录，无需已有 loopy）
    ↓
bootstrap 启动
    ↓
harness 体系落入 .loopy/graph/
    ↓
dashboard 模板落入 .loopy/dashboard/
    ↓
PREFERENCES.md 创建
    ↓
AI 可立即接手：按 graph 节点完成项目部署与实践
```

## 为什么需要

| 情况 | 做法 |
|------|------|
| 新项目，从零开始 | bootstrap → AI 按 graph 完成部署 |
| 已有项目，想接入 loopy | bootstrap 落 harness → AI 分析并部署 |
| 已有 loopy 的项目 | 跳过 bootstrap，直接走 graph 标准流程 |

**核心思想：harness 先落地，AI 再干活。** 没有 harness 的项目，AI 不知道"做到哪算对"。bootstrap 就是把验收标准先放进去。

## 落什么

```yaml
bootstrap:
  target: "{项目根目录}/.loopy/"

  landing_files:
    # graph 核心 —— harness 验收体系
    graph:
      - graph/GRAPH.md                # 项目级 graph 定义
      - graph/HARNESS.md              # harness 系统说明
      - graph/nodes/*.md              # 全部节点定义（8+1 个节点）
      - graph/harnesses/*.harness     # 全部 harness 验收文件

    # dashboard —— 可视化 + 文档
    dashboard:
      - dashboard/index.html          # Graph AI 触发点
      - dashboard/PROJECT.md          # 项目概览（从模板生成）
      - dashboard/REQUIREMENTS.md     # 需求追踪（从模板生成）
      - dashboard/VERSIONS/           # 版本演进目录

    # 根目录
    root:
      - PREFERENCES.md                # 偏好与约束
```

## 怎么做

```yaml
bootstrap:
  1_verify_target:
    - 确认目标项目路径存在
    - 若 .loopy/ 已存在，询问覆盖还是跳过
  2_land_harnesses:
    - 复制 graph/ 全部内容到 .loopy/graph/
    - 包括 nodes/ 和 harnesses/ 子目录
    - harness 文件是核心：每个节点对应一个验收合约
  3_init_dashboard:
    - 复制 dashboard/index.html
    - 从 PROJECT_TEMPLATE.md 生成 PROJECT.md（填入项目名）
    - 从 REQUIREMENTS_TEMPLATE.md 生成 REQUIREMENTS.md
    - 创建 VERSIONS/ 目录
  4_create_prefs:
    - 创建 PREFERENCES.md
    - 写入默认偏好：语言、commit 风格、部署方式
  5_report:
    - 列出已落地的文件清单
    - 告知 AI 后续可用的 graph 节点
    - 提示：harness 已就绪，可以开始部署实践
```

## 关键规则

```text
1. harness 必须完整落地 —— 缺一个节点就缺一个验收标准，AI 无法保证质量
2. 不覆盖已有的 PROJECT.md / REQUIREMENTS.md —— 若已存在则跳过
3. 不覆盖已有的 PREFERENCES.md —— 偏好是用户资产
4. bootstrap 是一次性的 —— 第二次跑应跳过或提示覆盖
5. 完成后必须报告：哪些文件新创建、哪些跳过、AI 可以开始做什么
```

## 与项目部署的关系

bootstrap 完成后，AI 可以立即按以下链路完成项目部署：

```text
understand（理解项目现状）
    ↓
verify（验证基础设施：能跑起来吗？测试通吗？）
    ↓
deploy 建议（根据项目栈给部署方案）
    ↓
dashboard（记录部署结果到演进史）
    ↓
record（写入日志）
```

实际上，bootstrap 之后的第一个任务通常就是「让这个项目部署跑通」，而 harness 体系保证了每一步都有验收标准。

## 与其它节点的关系

```text
bootstrap（项目初始化，落 harness）
    ↓
skill_import（导入 graph-engineer skill）
    ↓
repo_analyze / bootstrap skill（分析或建图）
    ↓
标准链路：understand → verify → package → dashboard → record → sync
```

bootstrap 是**所有节点的前置**。没有 bootstrap，其它节点没有 harness 可验证。

## CLI / Tool

```bash
# 对项目执行 bootstrap
loopy project init <path>

# 等同于（兼容旧语义）
loopy graph init --with-harnesses <path>

# 仅刷新 harness（不覆盖项目文档）
loopy harness update <path>
```

| tool | 作用 |
|------|------|
| `loopy.project_init` | bootstrap 全部内容到项目 |
| `loopy.harness_update` | 仅刷新 harness 文件，不动项目文档 |

## 不做的事

- 不分析项目代码（那是 repo_analyze 的事）
- 不创建 git commit
- 不在 bootstrap 时跑测试或部署
- 不覆盖用户已有的 PROJECT.md / REQUIREMENTS.md / PREFERENCES.md
