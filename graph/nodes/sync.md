---
name: sync-node
description: 同步节点。push 代码到远端，通知相关人员。不改代码，只推送。
node: sync
order: 5
---

# Sync Node — 同步节点

## 干什么

把 commit 推送到远端。

## 步骤

```text
1. 确认 commit 已经完成（package 节点产出）
2. git push
3. 如果有 CI/CD，等结果
```

## 输出格式

```text
## 同步结果

已推送到 origin/main（commit abc1234）。

CI 状态：等待中 / 通过 / 失败（附链接）
```

## 不做的事

- 不 force push
- 不改 git config
- 不操作 main/master 以外的分支（除非用户指定）

## 核心规则

```text
只 push，不改东西。
push 前确认 commit message 没问题。
```
