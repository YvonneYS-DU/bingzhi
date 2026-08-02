# Loopy 2.0 — Graph Engineer

从意图工程（loop engineer）升级为图工程（graph engineer）。

## loopy 1.0 的问题

1. **AI 理解用户会出错**。尤其是 Grok 这类模型，过度解读用户意图。
2. **层级太多**。7 层 L0-L7 大部分不需要。
3. **一步步追问拖住项目**。L7 Proactive Following 让 agent 不停问问题。
4. **偏好没地方存**。AI 不懂用户偏好时会乱猜。
5. **领导看不懂项目进展**。没有演进记录，新需求为什么是新需求说不清楚。

## loopy 2.0 的设计

两个引擎 + 偏好文件 + 项目仪表盘：

### Graph Engine（干活的）

```
启动 → 读 PREFERENCES.md
项目初始化 → 创建 PROJECT.md（探索、边界）
改代码前 → understand（建基线）
改代码后 → understand → verify → package → dashboard → record → sync
```

### Loop Engine（兜底的）

区分两种追问：
- **合理追问**：第一次遇到偏好 → 问一次 → 记 PREFERENCES.md
- **卡住信号**：连续追问、发明概念 → Loop 介入

### PREFERENCES.md

用户直接说的偏好，原样记录。问一次，永不再问。

### Dashboard（给领导看的）

纯静态 HTML 仪表盘。三个 Tab：
- **项目概览**：技术边界、初始探索、为什么选这条路
- **版本演进**：时间线 + 每个版本做了什么、测了什么、遇到什么问题
- **需求追踪**：新需求、完成情况、为什么新需求不是旧需求的延续、部署建议

## 目录结构

```
loopy/
├── README.md
├── PREFERENCES.md           # 项目偏好
├── graph/                   # Graph Engine
│   ├── GRAPH.md             # graph 引擎核心
│   └── nodes/
│       ├── understand.md    # 理解节点
│       ├── verify.md        # 验证节点
│       ├── package.md       # 封装节点
│       ├── dashboard.md     # 仪表盘节点
│       ├── record.md        # 记录节点
│       └── sync.md          # 同步节点
├── dashboard/               # 项目仪表盘
│   ├── index.html           # 可视化仪表盘（给领导看）
│   ├── PROJECT_TEMPLATE.md  # 项目概览模板
│   ├── VERSION_TEMPLATE.md  # 版本记录模板
│   └── REQUIREMENTS_TEMPLATE.md  # 需求追踪模板
└── loop/                    # Loop Engine
    └── LOOP.md              # loop 兜底
```

## 使用方式

把 `loopy/` 放到项目根目录。agent 加载后自动：

1. 启动时读 `PREFERENCES.md`
2. 项目初始化时创建 `PROJECT.md`（边界、探索）
3. 改代码前后跑 graph
4. 每次改完更新 dashboard（VERSIONS、REQUIREMENTS）
5. 卡住了 loop 介入

查看仪表盘：`cd dashboard && python3 -m http.server 8080`
