# Bands

化身读的是几条并行带，不是 `root → domain → project` 的树。

带与带没有父子关系。`identity` 不是 `ledger` 的父节点。`lesson` 不是 `trace` 的摘要文件夹。同一事实可以同时以不同密度存在于两条带上，靠 MAP 互指。

多具化身读同一组带。不要为每个 agent 复制一套。

## 六带

| 带 | 记什么 | 粒度 | 刷新 | 默认进不进这一具 |
|---|---|---|---|---|
| `working` | 此刻正在消费的活核 | 一词或短句 | 主题一变就换 | 只进仍在用的 |
| `ledger` | Goal / Core / Verified / Open / Next | 短标注行 | 每个接缝 | `loop` 必读 |
| `trace` | 近几日事件、带诊断的失败、未折叠中间态 | 事件行 | 折叠后可丢 | 只在 resume 或排障时 |
| `semantic` | 已验证教训、稳定决策 | 一句事实 | 结算时覆盖更新 | MAP 点名再读 |
| `invariant` | 硬约束、命名、风格锚、禁区 | 可执行短句 | 仍在约束动作时；红线后立刻 | 开会话读相关条 |
| `identity` | 是什么 / 不是什么 / 完成定义 | 一页 | 定位变了才改 | 开会话读 MAP + 本页 |

层次按时间尺度和表征密度切，不按目录归属切。

## MAP

`MAP.md` 只回答三个问题：默认读谁、某类问题去哪一带、哪些条目互指。

它是寻路，不是目录树，也不是把所有带拉进一具身体的许可证。

```markdown
# MAP

## default_load
- identity
- invariants
- working

## seek
- 卡住 / 隔天接着做 / 换执行者 → ledger + traces/current
- 改代码前怕漂 → 相关 invariant + working
- 同类问题是不是踩过 → lessons
- 这项目到底是什么 → identity

## links
- lesson:L-003 ↔ trace:YYYY-MM-DD-slug
```

## 加载规则

检索词命中不是加载许可。能进这一具的，必须是当前动作立刻要用的。

不要一次读六带。`fast` 零带，`full` 一两句，`loop` 先 MAP 再按 seek 加一带。

## 和 VLA 的对照（只为理解）

- `working` ≈ 当前工作记忆
- `trace` ≈ 短程稠密
- `semantic` ≈ 长程压缩
- `ledger` ≈ 非马尔可夫进度，也是可移交的化身
- `invariant` ≈ 必须保持点亮的约束
- MAP ≈ 先问需要哪一带，再读那一带

不要把这个对照当成要训练的模型。
