# 📕 XHS-Post v2.0 — 小红书纯钩子全自动发布

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Xiaohongshu-ff2449?style=for-the-badge" alt="platform">
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="python">
  <img src="https://img.shields.io/badge/Strategy-Pure_Hook-ff6b6b?style=for-the-badge" alt="hook">
  <img src="https://img.shields.io/badge/Multi_Account-✅-success?style=for-the-badge" alt="multi-account">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="license">
</p>

<p align="center">
  <b>🇨🇳 纯钩子策略 · 标题零业务暴露 · 多账号全自动 | 🇬🇧 Pure Hook Strategy · No Product Keywords · Multi-Account</b>
</p>

---

## 🔥 v2.0 重大更新 (2026-06-01)

### 纯钩子标题策略

**标题完全看不出业务类型**，只靠好奇心/情绪/悬念吸引点击：

```
✅ v2.0 标题：
  "发现了一个好东西……😭"
  "苏州人才知道的宝藏地方"
  "闺蜜说我太会过日子了"
  "发了朋友圈被问疯了"
  "不用买！不用买！不用买！"

❌ v1.x 标题（已废弃）：
  "我是真后悔租了这辆轮椅"
  "家里有老人的看过来"
```

### 核心铁律

| 规则 | v1.x | v2.0 |
|------|------|------|
| 标题暴露品类词 | ✅ 允许 | ❌ **严禁** |
| 标签 | #轮椅出租 #轮椅租赁 | #苏州生活 #宝藏分享 |
| 正文 | 直接说明服务 | 悬念故事→评论互动转化 |
| 多账号 | 不支持 | ✅ 双号轮流发布 |

---

## 🚀 快速开始

```bash
# 1. 设置Cookie
echo "your_cookie_string" > ~/.hermes/data/xhs_cookie_latest.txt

# 2. 准备素材（每个子文件夹5张图=1帖）
# D:\...\大宝小红书\57\  ← 5张图片

# 3. 发布
python xhs_publish.py

# 4. 指定文件夹发布
python xhs_publish.py 48
```

## 👥 多账号发布

```bash
# 账号1
cp ~/.hermes/data/xhs_cookie_玲丽.txt ~/.hermes/data/xhs_cookie_latest.txt
python xhs_publish.py

# 账号2
cp ~/.hermes/data/xhs_cookie_直租.txt ~/.hermes/data/xhs_cookie_latest.txt
python xhs_publish.py
```

## 📋 标题池（27条纯钩子）

| 类型 | 数量 | 示例 |
|------|------|------|
| 悬念型 | 7条 | "发现了一个好东西……😭" |
| 情绪型 | 5条 | "后悔没早点知道系列😭" |
| 反常识型 | 5条 | "不用买！不用买！不用买！" |
| 场景型 | 5条 | "去了趟医院才知道这东西能…" |
| 社交证明 | 3条 | "发了朋友圈被问疯了" |
| 短平快 | 2条 | "太香了！" "绝了！" |

## 🏗️ 技术栈

- **xhs** Python SDK — 纯Python签名引擎
- **无浏览器** — 不需要Playwright/扫码
- **Cookie动态读取** — 过期只需更新一个文件
- **已用标题去重** — 追踪最近20条

## 📁 文件结构

```
.
├── xhs_publish.py          # 主发布脚本（27条纯钩子标题池）
├── SKILL.md                # Hermes技能文档
├── README.md               # 本文件
├── requirements.txt        # xhs
└── references/
    ├── xhs-cookie-format.md
    ├── xhs-cookie-management.md
    ├── cron-silent-failure-diagnosis.md
    └── environment-setup.md
```

## 📜 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.0 | 2026-06-01 | 纯钩子策略：标题/正文/标签零业务暴露，多账号支持 |
| v1.1 | 2026-05-29 | 38条动态标题池，去重追踪 |
| v1.0 | 2026-05-25 | 从crosspost拆分，独立为小红书专用 |

## 👤 作者

**大宝 (DaBao)** — 昆山佳康顺医疗器械新媒体运营负责人

---

<p align="center">
  <b>📕 标题不说产品，只说故事——让用户自己发现答案。</b>
</p>
