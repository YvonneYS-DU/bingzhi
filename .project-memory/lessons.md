# Lessons

- L-001 ✓ 问一次的偏好写入 PREFERENCES.md，不要写进对话总结
  why: 同类问题反复问 = 没落盘
  when: 用户纠正行为时

- L-002 ✓ AI 理解用户会出错，尤其不要让它揣测意图
  why: loopy 1.0 七层意图工程拖住项目，2.0 砍成 graph + loop
  when: agent 开始发明概念或连续追问时

- L-003 ✓ 每一步追问会拖住项目
  why: 连续追问是 bug，不是谨慎
  when: 出现「我需要了解更多」但已经问过 2 次

- L-004 ✓ 无 graph 的 repo 先出 temporary 构建历史
  why: 补历史不是冒充正式发版
  when: 用户选中一个还没有 graph 的 folder

- L-005 ✓ 四类推理损失不是可计算公式，是接缝上的协议探针
  why: J-Space 自己也写了不能从分数反推二极管贡献，也不能做因果分解
  when: 有人把 overload/drift/retry/done 当成指标来「算」

- L-006 ✓ 能力实现栈是六层；四类损失只覆盖后三层（活动表征 / 长程状态 / 验证）
  why: 缺入口层时会觉得协议不完整——首轮接口、工具 schema、轨迹选择不在四类里
  when: 设计记忆或控制协议时

- L-007 ✓ J-Space 是推理时控制层，封装成 skill；不是训练，也不是 loopy 那种节点验收 harness
  why: 原文写明不改权重、不微调；可选 jspace.py 只记账本，不选解法
  when: 有人把它当成模型升级或测试框架

- L-008 ✓ 思诚管认识状态能否当前提；J-Space 管工作台如何加载、保持、验证
  why: observed/inferred/unknown ≈ ✓/?/✗，但思诚不外化 Goal/Core/Next，也不做入口轨迹锁定
  when: 想合并两套协议，或觉得「很像所以可以互相替代」

- L-009 ✓ 项目记忆吸收 J-Space 思想，但不锁死核心数
  why: 过载判据是点名失败或重推导已写约束，不是事先规定几个槽
  when: 写 working / ledger.Core，或有人把「两个核」当成配额

- L-010 ✓ 思诚是道，身外化身是术；未来多 agent 读同一份外化状态
  why: 化身不是第二个我，是可移交的工作台
  when: 起名、分 skill、或准备把状态交给另一执行者
