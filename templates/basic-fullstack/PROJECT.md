# 基础前后端 Graph Engineer 模板

> 这是一个 Graph Engineer Panel 模板，用于通过 AI 创建/更新项目架构图。

## 这是什么

一个独立的 Graph Engineer 仪表盘（`panel.html`），不是可运行的前后端应用代码。

- 包含架构图可视化（节点 / 边 / 版本时间轴）
- 包含 AI 助手面板（4 个 Skill），可通过 AI 操作：
  - **SKILL 01**：bootstrap - 启动版本 + 创建图
  - **SKILL 02**：iterate - 版本迭代 + 更新图
  - **SKILL 03**：diff_boss - 看变化 / 给老板讲差异
  - **SKILL 04**：repo_history - 选中 repo 构建临时版本历史
- 默认图：用户 → 前端 → 后端 → 数据库（基础全栈架构）

## 使用方式

```bash
# 本地预览
cd templates/basic-fullstack
python3 -m http.server 8080
# 打开 http://localhost:8080/panel.html
```

或直接用浏览器打开 `panel.html`。

点击右下角 **AI 助手** 按钮，进入 AI 面板创建/更新架构图。

## 技术边界

| 项 | 说明 |
|----|------|
| 类型 | 纯静态 HTML（零依赖、零构建） |
| 数据 | JS 内嵌（TEMPLATE_ARCH / ARCH），无后端 |
| AI | 本地 Demo 模拟；接 agent 后可写 draft 文件落盘 |
| 项目切换 | 顶栏「基础前后端」/「会议室预定」切换不同 graph 数据 |

## 自定义

1. 修改 `TEMPLATE_ARCH` 节点/边/版本数据
2. 或通过 AI 面板（点 AI → 输目标 → AI 模拟写图）
3. 接真实 agent 后：AI 直接操作 DOM 或写 `VERSIONS/draft-*.md`
