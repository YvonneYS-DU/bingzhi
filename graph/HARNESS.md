---
name: harness-system
description: 每个标准图节点都有对应的 harness 文件。graph 本身是 harness 的 harness —— 编排执行顺序、校验节点间数据合约。
status: active
---

# Harness System — 节点验收与合约系统

## 是什么

每个 graph 节点对应一个 `.harness` 文件，定义三件事：

```text
1. 输入合约   — 这个节点运行需要什么数据
2. 输出合约   — 这个节点运行完应该产出什么
3. 验收规则   — 怎么判定"通过了"
```

graph 作为"harness 的 harness"，负责：

```text
1. 按顺序编排节点
2. 节点间数据合约校验（上一个节点的输出是否满足下一个节点的输入合约）
3. 切版本时自动归档 harness 快照
```

## 不是什么

- 不是测试框架（不做 E2E / 集成测试 / 性能测试）
- 不是生命周期管理系统（不跟踪 draft → active → stable 状态）
- 不是进化引擎（不收集反馈、不自动改进 harness 本身）
- 不是迭代循环系统（跨轮次评估迭代由后续 skill 处理）

**只做一件事：每个节点跑之前知道要什么，跑之后知道对不对。**

## 文件结构

```
graph/
├── GRAPH.md                      # 图定义 + harness 源声明
├── HARNESS.md                    # 本文件
├── nodes/                        # 节点定义（做什么）
│   ├── understand.md
│   ├── verify.md
│   ├── package.md
│   ├── dashboard.md
│   ├── record.md
│   ├── sync.md
│   ├── skill_import.md
│   └── repo_analyze.md
└── harnesses/                    # 节点验收（怎么验证）
    ├── understand.harness
    ├── verify.harness
    ├── package.harness
    ├── dashboard.harness
    ├── record.harness
    ├── sync.harness
    ├── skill_import.harness
    └── repo_analyze.harness

.loopy/snapshots/                 # 切版本时自动归档的快照（AI 不读，除非用户明确指令）
    ├── v1/
    │   ├── understand.harness
    │   └── ...
    └── v2/
        ├── understand.harness
        └── ...
```

## .harness 文件格式

每个 `.harness` 文件包含以下部分：

```yaml
# 输入合约 — 这个节点需要什么才能运行
input:
  required:                       # 必填，缺一不可
    - field_name: type
  optional:                       # 可选，有则更好
    - field_name: type

# 输出合约 — 这个节点运行后产出什么
output:
  - field_name: type

# 验收规则 — 怎么算通过
validation:
  - 规则描述（自然语言，供 agent 自检）

# 失败策略
on_failure: block | warn | skip   # block=阻断链路，warn=记录但继续，skip=跳过
```

### on_failure 三种策略

| 策略 | 行为 | 适用节点 |
|------|------|---------|
| `block` | 阻断链路，停止后续节点 | 核心质量门禁（understand、verify、sync、skill_import） |
| `warn` | 记录失败但继续 | 辅助节点（package、dashboard、record、repo_analyze） |
| `skip` | 跳过不执行 | 可选节点（暂无） |

## Harness 源声明

- **唯一源：`graph/harnesses/`** —— 所有节点只从这里读 harness 定义
- **`.loopy/snapshots/`** 是自动归档。只有 `dashboard` 节点在切版本时写入，其他节点不读
- 需要对比历史版本时，**用户明确指令**才读快照（如"v1 的 verify 验收标准是什么"）

## 与 revfactory/harness 的关系

借鉴了以下概念：

| 借鉴 | loopy 落地方式 |
|------|--------------|
| 每个 agent 有明确的 I/O 协议 | 每个节点的输入/输出合约 |
| 结构校验 + 执行测试 | 验收规则（validation） |
| 失败策略（block vs warn） | on_failure: block | warn | skip |
| Phase 之间数据传递 | 节点间合约校验 |

明确不引入的：

| 不引入 | 原因 |
|--------|------|
| 进化机制（change_log, feedback loop） | loopy 1.0 证明过早加会拖慢项目 |
| 生命周期管理（draft → active → stable） | 已有 dashboard/VERSIONS 管版本 |
| Phase 0 审计分叉 | 先假设全量跑，够简单 |
| 执行模式选择（team/subagent/hybrid） | graph 就是 Pipeline，不需要选择 |
| 触发器验证（should/should-not trigger） | loopy 没有 skill marketplace，不需要 |
| CLAUDE.md 指针注册 | loopy 用 GRAPH.md 代替 |
| 迭代循环（retry） | 跨轮次评估迭代由后续 skill 处理，harness 只做单次验收 |

## 核心原则

```text
每个节点跑之前知道要什么，跑之后知道对不对。
不发明概念，不拖住项目。
先跑通默认链路，再谈自定义。
```
