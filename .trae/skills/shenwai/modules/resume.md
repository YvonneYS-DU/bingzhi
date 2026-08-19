# Resume

长间隔之后，或换了一具化身之后，账本还在，前提会淡。禁止凭印象接着改。

## 顺序

不要跳：

1. 读 `MAP.md`
2. 读 `identity.md`
3. 读仍可能约束动作的 `invariants.md`
4. 若存在未完成 `ledger.md`，**整份重读**，不要只读最后一行
5. 读 `working.md`。与 ledger.Core 冲突时，以更新更晚且带 `✓` 的为准
6. 用一句话重述当前 Goal 和 Next，再动手
7. 只有排障、隔天续做、换执行者对不上、用户问「上次怎么了」时，才读 `traces/current.md`

## 回来时要能说清

- 完成条件还是不是原来那句
- 此刻身体里真正在用的核
- 下一条动作是什么
- 哪几条 Open 还开着
- 上一具留下的诊断，这一具有没有接着用

说不清，先把账本补到能说清，再工作。

## 首次落地

对一个还没有 `.project-memory/` 的仓库：

1. 按 `templates/` 建空壳
2. 从 README、PREFERENCES、已有项目说明里 **只摘已经写明的事实** 填 identity / invariants
3. 写 MAP 的 default_load 与 seek
4. 不回填历史对话
5. 把 `ledger.md`、`working.md`、`traces/` 加进 `.gitignore`

之后每次长任务走门控，不要每次重建系统。多具化身继续共用这一份外化状态。
