---
name: skill-import-node
description: 导入 graph-engineer skill 后展开为前后端能力。Cursor 发消息写入；HTML Graph AI 成为触发点。
node: skill_import
order: 0
---

# Skill Import Node — Skill 导入节点

## 干什么

默认导入技能名：**graph-engineer**（`.trae/skills/graph-engineer`）。

倒入后不再只是一段提示词，而是展开成可运行的前后端形态，并接上 Cursor 写入通道 + HTML 触发点。

```text
导入 skill
    ↓
生成 / 绑定 前后端
    ↓
Cursor 发消息
    ↓
写入 PROJECT / VERSIONS / REQUIREMENTS / 日志
```

## 输入

| 输入 | 说明 |
|------|------|
| skill 路径或内容 | `.trae/skills/<name>/SKILL.md` 或用户指定的 skill 包 |
| 目标项目根目录 | loopy 所在或要接入的 repo |
| 可选偏好 | 是否已有 `PREFERENCES.md` |

## 输出

| 输出 | 说明 |
|------|------|
| 后端能力 | skill 规则变成可调用的 graph / API / 写入接口 |
| 前端能力 | dashboard 或对话侧可操作入口（看演进、选 repo、看版本） |
| 写入通道 | Cursor 消息 → 结构化落盘 |

## 展开规则

```yaml
skill_import:
  1_parse:
    - 读 SKILL.md frontmatter（name, description）
    - 读 body 指令与约束
  2_bind_graph:
    - 把 skill 行为挂到现有 graph 节点（understand / verify / dashboard / record…）
    - 缺节点就按标准图补默认节点，不发明新抽象
  3_expose:
    frontend:
      - dashboard 展示
      - 对话区可选 repo / 看临时版本
    backend:
      - 消息写入接口
      - 版本 / 需求 / 日志落盘
  4_wire_cursor:
      - Cursor 用户消息进入 write_channel
      - 只写事实：需求、改动、决策、版本草稿
```

## Cursor 写入通道

Cursor 里发消息时，agent 按消息类型写入：

| 消息类型 | 写入哪里 | 例子 |
|---------|---------|------|
| 新需求 / 目标 | `REQUIREMENTS.md` | 「下周要做数据看板」 |
| 偏好 / 约束 | `PREFERENCES.md` | 「commit 用英文」 |
| 完成一轮改动 | `VERSIONS/v{N}.md` + record 日志 | 大改动后自动 |
| 探索 / 边界 | `PROJECT.md` | 项目初始化或边界变化 |
| 对某 repo 的分析结论 | `VERSIONS/draft-*.md`（临时版本） | 见 repo_analyze 节点 |

### 写入原则

```text
1. 用户原话优先，不脑补
2. 能归类就归类；归不了就先记 record 日志
3. 一次消息只写该写的文件，不刷屏
4. 已有条目就更新状态，不重复堆砌
```

## CLI / Tool

```bash
# 导入 skill 并绑定到当前项目
loopy skill import <skill-path-or-name>

# 查看已导入 skill 与写入通道状态
loopy skill list

# 手动把一条 Cursor/对话消息写入（一般由 agent 自动调）
loopy write --type requirement|preference|version|log --message "..."
```

对应 tool 名称（给 agent 调）：

| tool | 作用 |
|------|------|
| `loopy.skill_import` | 解析 skill，绑定 graph，暴露前后端 |
| `loopy.write` | 按类型把消息写入 dashboard 文件 |
| `loopy.skill_status` | 当前绑定了哪些 skill、写到哪 |

## 不做的事

- 不把 skill 再包一层「意图引擎」
- 不在导入时追问一堆配置；缺省用 graph 默认图
- 不把 Cursor 闲聊全部落盘；只落可归类的项目信息

## 核心规则

```text
Skill 倒入 = 前后端能力 + 写入通道。
Cursor 说话 = 能归类就写入。
先能跑通默认图，再谈自定义。
```
