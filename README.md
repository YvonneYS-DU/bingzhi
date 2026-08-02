# Loopy 2.0 — Graph Engineer

从意图工程升级为 **Graph Engineer**（图工程）。

技能包：`.trae/skills/graph-engineer/SKILL.md`

## 设计要点

### 1. 技能名：graph-engineer

导入后在 Cursor / Graph AI 使用四个场景：

| | 场景 |
|--|------|
| SKILL 01 | Bootstrap version + create graph |
| SKILL 02 | Iterate version + update graph |
| SKILL 03 | What changed / how it differs（给领导） |
| SKILL 04 | **选中 repo → 临时版本历史**（无 graph 的仓库补历史） |

### 2. 无 graph 的 repo 也能构建历史

在截图/Graph AI 里 **选中文件夹 repo → 提问 → AI 分析 → 按 repo 生成版本迭代**。  
这些版本标记为 **temporary**，用来给从没建过 graph 的仓库补「构建历史」。确认后再 promote 成正式 `v{N}`。

### 3. HTML 是 AI 触发点

`dashboard/index.html` 不只是展示：

```text
选中 repo folder → 问 AI → AI 分析 → AI 写创建图表（节点/边/TEMP 时间轴）
```

本地预览：

```bash
cd dashboard && python3 -m http.server 8080
# 打开 http://localhost:8080 → 点 AI → 选文件夹 → SKILL 04
```

## Graph 流程

```
启动 → PREFERENCES.md
初始化 → PROJECT.md
Graph AI → bootstrap / iterate / diff / repo_history(temporary)
改代码前 → understand
改代码后 → understand → verify → package → dashboard → record → sync
```

## 目录

```
loopy/
├── .trae/skills/graph-engineer/SKILL.md
├── cli/LOOPY_CLI.md
├── graph/GRAPH.md
├── graph/nodes/          # 含 skill_import、repo_analyze
├── dashboard/index.html  # 触发点 + 图
├── dashboard/VERSIONS/   # vN + draft-*
└── loop/LOOP.md
```

## CLI（语义）

```bash
loopy skill import graph-engineer
loopy repo analyze <path>
loopy version promote draft-v1 --as v1
loopy write --type ...
```

## Loop 兜底

能做就不问。偏好问一次写入 `PREFERENCES.md`。连续追问 / 发明概念 → Loop 介入。
