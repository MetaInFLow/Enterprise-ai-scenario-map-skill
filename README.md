# 🗺️ 企业AI场景地图生成器 | Enterprise AI Scenario Map Generator

**"老板，我们公司到底哪里能用AI？" —— 这个问题，现在有答案了。**

**"Boss, where exactly can we use AI?" — Now there's an answer.**

---

每个企业都知道AI很重要，但90%的老板面对的现实是：

- 🤷 "AI到底能帮我做什么？" —— 听了100场演讲，还是一头雾水
- 💸 "我该先投哪个方向？" —— 怕投错钱，更怕错过窗口期
- 📊 "别人都在用AI了？" —— 焦虑但不知道从哪开始

Every company knows AI matters, but 90% of business leaders face this reality:

- 🤷 "What can AI actually do for me?" — Attended 100 talks, still confused
- 💸 "Where should I invest first?" — Afraid of wasting money, more afraid of missing the window
- 📊 "Everyone else is using AI already?" — Anxious but don't know where to start

**这个工具就是为此而生。** 它是一个 AI Agent Skill，能为任何企业自动生成一份 15-30 页的「AI场景地图报告」——从深度调研到场景识别，从优先级排序到落地路径，一气呵成。

**This tool was built for exactly this.** It's an AI Agent Skill that auto-generates a 15-30 page "AI Scenario Map Report" for any company — from deep research to scenario discovery, from priority ranking to implementation roadmap, all in one go.

---

## ✨ 这份报告长什么样？| What's in the Report?

| 章节 Part | 内容 Content | 页数 Pages |
|:---:|---|:---:|
| **封面** Cover | 客户名称、日期、编制单位 | 1 |
| **Part 1** 执行摘要 | 一页纸讲清楚：你是谁、痛在哪、AI能帮什么、从哪开始 | 1 |
| **Part 2** 企业画像 | 企业速写、业务价值链、业务特性分析、核心痛点诊断 | 3-4 |
| **Part 3** 行业扫描 | 3个行业标杆AI实践案例 + 可借鉴的启示 | 2 |
| **Part 4** 场景地图 | **30+ 个AI应用场景**全量清单 + 优先级矩阵 + 3个重点场景深度解读 | 5-6 |
| **Part 5** 实施路径 | 3阶段落地计划 + 关键成功要素 | 2 |
| **Part 6** 下一步 | 服务能力 + 行动建议 | 1 |

> 不是PPT废话，是能拿去开会拍板的东西。
>
> Not empty slides — something you can bring to a board meeting and make decisions with.

---

## 🚀 快速开始 | Quick Start

### 前置要求 Prerequisites

- 一个支持 **web-search** 工具的 AI Agent（如 Claude Code、ChatGPT with browsing 等）
- Python 3.8+（用于运行调研框架生成脚本）
- An AI Agent with **web-search** capability (e.g., Claude Code, ChatGPT with browsing, etc.)
- Python 3.8+ (for the research framework generator script)

### 使用方式 Usage

1. **克隆仓库 Clone**
   ```bash
   git clone https://github.com/YuanziAI/enterprise-ai-scenario-map.git
   cd enterprise-ai-scenario-map
   ```

2. **在你的 AI Agent 中加载 Skill**
   将 `SKILL.md` 加载到你的 AI Agent 中（不同平台加载方式不同）

   **Load the Skill into your AI Agent** — load `SKILL.md` (method varies by platform)

3. **开始使用 Start**
   ```
   帮我为"XX有限公司"生成一份AI场景地图报告
   ```
   或者 / or:
   ```
   Generate an AI scenario map report for "XX Company"
   ```

### 三种模式 Three Modes

| 模式 Mode | 适用场景 When to Use | 场景数 Scenarios | 报告页数 Pages |
|:---:|---|:---:|:---:|
| 🏃 **快速扫描** Quick Scan | 先看看AI能帮什么 | 15-20 | 5-8 |
| 📋 **标准报告** Standard | 完整的AI落地规划 | 30+ | 15-20 |
| 🔬 **深度规划** Deep Plan | 详细落地方案 + ROI | 50+ | 20-30 |

---

## 📂 项目结构 | Project Structure

```
enterprise-ai-scenario-map/
├── SKILL.md                        # 🧠 核心 Skill 定义（Agent 读这个）
├── scripts/
│   └── deep_research_wrapper.py    # 🔧 调研框架生成脚本
├── references/
│   ├── report-template-v2.1.md     # 📄 V2.1 报告模板
│   ├── business-analysis-framework.md  # 📊 业务分析框架
│   ├── typical-ai-scenarios.md     # 🤖 8大行业典型AI场景库
│   ├── scenario-priority-framework.md  # ⚖️ 优先级评估框架
│   ├── industry-case-template.md   # 📝 行业案例模板
│   └── company-info-config.md      # 🏢 编制单位信息配置
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🔧 工作原理 | How It Works

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  阶段1       │     │  阶段2        │     │  阶段3        │     │  阶段4        │
│  Deep        │ ──▶ │  Analysis &  │ ──▶ │  Scenario    │ ──▶ │  Report      │
│  Research    │     │  Diagnosis   │     │  Mapping     │     │  Generation  │
│  深度调研     │     │  分析诊断     │     │  场景地图     │     │  报告生成     │
└─────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
  🔍 web-search       📊 框架分析          🗺️ 30+场景           📋 V2.1模板
  企业信息              业务特性             优先级矩阵            6个Part
  行业痛点              痛点诊断             重点场景              15-30页
  标杆案例              对标启示             实施路径
```

**关键设计**：脚本只负责生成「调研框架 + 搜索问题清单」，实际的深度调研由 AI Agent 通过 web-search 工具完成。这意味着：
- 零外部API依赖，零额外成本
- 调研质量取决于你的 Agent 能力
- 支持任何有 web-search 能力的 Agent 平台

**Key Design**: The script only generates a "research framework + search query list". The actual deep research is done by the AI Agent via web-search. This means:
- Zero external API dependencies, zero extra cost
- Research quality depends on your Agent's capability
- Works with any Agent platform that has web-search

---

## 🏭 已覆盖行业场景库 | Industry Scenario Library

内置 8 大行业的典型AI场景参考，开箱即用：

| 行业 Industry | 典型场景数 Scenarios |
|:---:|:---:|
| 🏗️ 建筑工程 Construction | 8+ |
| 🛒 电商零售 E-commerce | 8+ |
| 🏦 金融 Finance | 8+ |
| 🏭 制造 Manufacturing | 8+ |
| 🏥 医疗 Healthcare | 8+ |
| 🎓 教育 Education | 8+ |
| ⚖️ 法律 Legal | 8+ |
| 🚚 物流 Logistics | 8+ |

> 不在列表里的行业？没关系——Agent 会通过 web-search 实时调研，动态生成场景。
>
> Industry not listed? No problem — the Agent researches in real-time via web-search and generates scenarios dynamically.

---

## 🤝 贡献 | Contributing

欢迎 PR！特别欢迎：
- 新增行业场景库（在 `references/typical-ai-scenarios.md` 中添加）
- 优化报告模板
- 添加新语言支持
- 分享你用这个工具生成的精彩案例

PRs welcome! Especially:
- New industry scenario libraries
- Report template improvements
- New language support
- Sharing great reports generated with this tool

---

## 📜 License

[MIT License](LICENSE) — 随便用，记得给个 Star ⭐

MIT License — Use freely, and give us a Star ⭐ if it helps!

---

## 📬 联系我们 | Contact

| | |
|---|---|
| **公司** Company | 源子（深圳）人工智能有限公司 / Yuanzi AI |
| **联系人** Contact | Neil |
| **微信** WeChat | `838000702` |
| **公众号** Official Account | **源子AI Metainflow** |

---

> 🧠 *让每个企业都看得见自己的AI未来。*
>
> *Let every enterprise see its AI future clearly.*
