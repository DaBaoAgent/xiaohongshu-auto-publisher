# 📕 XHS-Post — 小红书全自动图文发布神器 / AI-Powered Xiaohongshu Auto Publisher

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Xiaohongshu%20|%20小红书-ff2449?style=for-the-badge" alt="platform">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="python">
  <img src="https://img.shields.io/badge/API-Pure_Python-success?style=for-the-badge" alt="api">
  <img src="https://img.shields.io/badge/Speed-30s-red?style=for-the-badge" alt="speed">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="license">
  <img src="https://img.shields.io/badge/Contributor-Dabao-orange?style=for-the-badge" alt="contributor">
</p>

<p align="center">
  <b>🇨🇳 纯Python API驱动，30秒极速发布，无需浏览器 | 🇬🇧 Pure Python API, 30s publish, no browser needed</b>
</p>

---

## 📖 中文 / English

### 🇨🇳 中文介绍

**小红书全自动图文发布神器** — 基于 `xhs` Python SDK 的纯API自动化发布工具。

不需要Playwright、不需要浏览器、不需要扫码——纯Python签名引擎直接调用小红书API，**30秒**完成一篇图文笔记发布。Cookie从统一文件动态读取，过期后只需更新一个文件，cron自动生效。

#### 🔥 核心特性

| 特性 | 说明 |
|------|------|
| ⚡ **30秒极速** | 纯API调用，无浏览器开销 |
| 🔑 **Cookie动态** | 从 `xhs_cookie_latest.txt` 统一读取，更新即生效 |
| 🚫 **零浏览器** | 不需要Playwright/Chromium，资源占用极低 |
| 🤖 **全自动** | 扫描素材库 → 选文件夹 → 生成文案 → 发布 → 标记已发 |
| 📁 **批量管理** | 文件夹即帖子，自动跳过已发标记 |
| 🪟 **Windows原生** | Windows 11 + Python 3.12+ |

#### 📊 发布节奏

每天2篇：`08:00 / 19:00`

#### 🚀 快速开始

```bash
# 1. 更新Cookie（过期时）
echo "你的Cookie" > ~/.hermes/data/xhs_cookie_latest.txt

# 2. 发布
python xhs_publish.py
```

---

### 🇬🇧 English

**Xiaohongshu Auto Publisher** — Pure Python API-driven publishing tool for REDnote (Xiaohongshu).

No Playwright, no browser, no QR code scanning — uses the `xhs` library's pure Python signature engine to call REDnote's API directly. **30 seconds** per post. Cookie is read dynamically from a unified file; update one file and cron picks it up automatically.

#### 🔥 Key Features

| Feature | Description |
|---------|-------------|
| ⚡ **30s Speed** | Pure API calls, zero browser overhead |
| 🔑 **Dynamic Cookie** | Reads from `xhs_cookie_latest.txt` — update once, works everywhere |
| 🚫 **No Browser** | No Playwright/Chromium needed |
| 🤖 **Fully Automated** | Scan → select → generate copy → publish → mark |
| 📁 **Batch Ready** | One folder = one post, auto-skip published |

#### 📊 Schedule

2 posts/day: `08:00 / 19:00` CST

#### 🚀 Quick Start

```bash
# Update cookie (when expired)
echo "your_cookie_string" > ~/.hermes/data/xhs_cookie_latest.txt

# Publish
python xhs_publish.py
```

---

## 🏗️ 架构 / Architecture

```
xhs-post/
├── README.md
├── xhs_publish.py              # 🟢 纯API发布（Cookie动态读取）
└── references/
    ├── xhs-cookie-management.md # 🔑 Cookie获取和保存流程
    ├── xhs-cookie-format.md     # Cookie格式规范
    └── environment-setup.md     # 环境配置指南
```

---

## 📊 实战数据 / Production Stats

| 指标 / Metric | 数据 / Value |
|------|------|
| 发布耗时 | ~30秒/篇 |
| 技术方案 | `xhs` 0.2.13 纯Python签名 |
| Cookie刷新 | 约1-3天一次 |
| 成功率 | >95%（Cookie有效时） |
| 典型错误 | `code: -100` → Cookie过期 |

---

## 🧩 技术栈 / Tech Stack

| 技术 | 用途 |
|------|------|
| `xhs` 0.2.13 | 小红书纯Python API客户端 |
| `sign(uri, data, a1=a1)` | 纯Python签名引擎 |
| `web_session` Cookie | 认证核心 |
| 动态文件读取 | Cookie热更新，cron自动生效 |

---

## 🔗 生态协作 / Ecosystem

```
xhs-post (独立素材，大宝小红书文件夹)
dy-post (复用闲鱼素材)
xianyu-post (闲鱼先发)
```

配套项目：**[xianyu-post](https://github.com/DaBaoAgent/xianyu-post)** | **[dy-post](https://github.com/DaBaoAgent/dy-post)**

---

## 🤝 贡献者 / Contributor

| 角色 | 贡献 |
|------|------|
| **大宝 / Dabao (徐海平)** | 产品Owner、需求、Cookie提供 |
| **Hermes Agent** | AI驱动全流程开发 |

---

## ⚠️ 免责声明

本项目仅供技术交流学习，请遵守小红书平台使用条款。

---

## 📄 License

MIT © [DaBaoAgent](https://github.com/DaBaoAgent)

<p align="center">
  <b>Made with ❤️ by Dabao & Hermes Agent</b><br>
  <sub>2026 · 佳康顺医疗器械 · 昆山</sub>
</p>
