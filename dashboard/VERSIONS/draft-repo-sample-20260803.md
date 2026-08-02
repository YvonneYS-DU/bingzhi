# draft — 无 graph 的 repo 构建历史（示例）

> 状态：temporary  
> 技能：graph-engineer · SKILL 04  
> 日期：2026-08-03  
> 来源 repo：/path/to/selected-repo（可从未使用过 graph）  
> 关联正式版本：确认后升格  
> 关联 commit：—  
> 触发：dashboard/index.html Graph AI 选中 folder

## 这是什么

给 **还没有 graph 历史** 的仓库补演进：AI 根据目录证据切片成临时版本，并写架构图。  
**不是**已经发生的正式发版记录。

## 分析基线

| 项 | 内容 |
|----|------|
| 主要栈 | 以扫描为准（示例：React + FastAPI） |
| 顶层目录 | frontend/ backend/ … |
| 已有 graph | 无 → 走构建历史 |

## 临时构建历史（可多条）

| draft | 含义 |
|-------|------|
| draft-v1 | 基线：主链路 / 边界 |
| draft-v2 | 下一迭代建议（仅建议） |

## 图表

HTML 触发后 AI 应：创建/更新节点与边，时间轴卡片标 **TEMP**。

## 如何升格

```bash
loopy version promote draft-v1 --as v1
```

---

*repo_analyze / Graph Engineer SKILL 04 · temporary until promoted*
