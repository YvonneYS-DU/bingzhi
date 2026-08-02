---
name: package-node
description: 封装改动。整理 commit、写 commit message、准备提交。不改代码，只整理。
node: package
order: 3
---

# Package Node — 封装节点

## 干什么

把改动整理成可以提交的 commit。不改代码，只整理。

## 步骤

```text
1. 看改动的文件列表
2. 分组（相关改动放一起）
3. 写 commit message
4. git add 相关文件
```

## Commit message 格式

```text
<type>: <一句话说清楚改了什么>
```

type 只有这几种：

| type | 什么时候用 |
|------|-----------|
| feat | 新功能 |
| fix | 修 bug |
| refactor | 重构，不改功能 |
| docs | 文档 |
| test | 测试 |
| chore | 配置、依赖等 |

示例：

```text
feat: foo() 支持 D 场景模式
fix: bar() 在空输入时崩溃
refactor: 把 foo() 的参数从位置参数改为关键字参数
```

## 输出格式

```text
## 待提交

### commit 1
feat: foo() 支持 D 场景模式

文件：
- src/foo.py（新增 mode 参数）
- src/bar.py（传入 mode="D"）
- tests/test_foo.py（新增 D 场景测试）

### commit 2（如果有）
...
```

## 不做的事

- 不自动 commit（让用户确认）
- 不改代码
- 不写长篇 commit body（除非用户要求）

## 核心规则

```text
一个 commit 只做一件事。
commit message 说清楚做了什么，用中文。
分组要合理：相关的文件一起提交，不相关的分开。
```
