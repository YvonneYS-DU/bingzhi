---
name: verify-node
description: 验证代码改动正确性。跑测试、检查 lint、确认项目能正常运行。不改代码，只检查。
node: verify
order: 2
---

# Verify Node — 验证节点

## 干什么

确认改动没坏。不改代码，只检查。

## 检查项

```text
1. 跑相关测试
2. 跑 lint / type check（如果有配置）
3. 检查有没有明显的遗漏（import 缺失、未定义的变量等）
```

## 输出格式

```text
## 验证结果

### 测试
- test_foo.py: 全部通过（12/12）
- test_bar.py: 全部通过（5/5）

### Lint
- 无新增警告

### 检查项
- import 完整
- 无未定义引用
```

如果有失败：

```text
## 验证结果

### 测试
- test_foo.py: 1 个失败
  - test_foo_with_mode_d: foobarAssertionError, 期望 B 但得到 D

建议：检查 foo() 在 mode="D" 时的返回值逻辑。
```

## 不做的事

- 不修 bug（修 bug 是改代码的事，验证节点只报告）
- 不判断设计好坏
- 不说"建议重构"

## 核心规则

```text
只报告事实：通过了什么、失败了什么。
失败了就说清楚哪一行、什么错误。
像 CI 日志一样简单直接。
```
