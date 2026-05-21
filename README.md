# 🚀 XHS-Post — 小红书全自动图文发布神器

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/小红书-API全自动-red.svg" alt="小红书">
</p>

<p align="center">
  <b>基于 xhs Python SDK 的小红书图文笔记全自动发布工具</b><br>
  支持 BLIP 本地图像识别 + AI 文案生成 → 30 秒完成一篇笔记发布<br>
  无需浏览器 · 无需手动操作 · 纯 API 自动化
</p>

---

## 📌 这能做什么？

如果你在小红书上运营内容，你一定知道：

- 😫 打开 App → 选图 → 写标题 → 写正文 → 加标签 → 发布... 一篇笔记至少 10 分钟
- 😫 每天发 3-5 篇，时间全花在重复操作上
- 😫 想批量发布但小红书没有开放 API... 

**XHS-Post 解决的就是这个问题。**

```bash
python xhs_publish.py --folder "./素材/今日OOTD" --title "被自己温柔到了～" --desc "..."
# 30秒后 → 笔记已发布
```

---

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🔐 **Cookie 自动验证** | 发布前校验账号归属，防止发错号 |
| 🖼️ **BLIP 本地识图** | 没有多模态 AI 也能分析照片内容，自动判断场景类型 |
| ✍️ **AI 文案生成** | 基于场景自动生成标题 + 正文 + 话题标签 |
| 🚀 **API 一键发布** | 纯 API 调用，30 秒完成，不需要打开浏览器 |
| 📂 **素材批量管理** | 自动扫描文件夹，发布后自动标记 |
| 🛡️ **先审后发** | 默认先展示文案给用户审核，确认后才发布 |

---

## 🎯 适用场景

- 🛍️ **电商卖家** — 批量发布商品种草笔记
- 👗 **穿搭博主** — OOTD 日常快速发布
- 🏠 **本地商家** — 探店/服务类内容自动化
- 🤖 **AI 代理** — 配合 LLM Agent 实现全自动内容运营

---

## ⚡ 5 分钟上手

### 1. 安装依赖

```bash
pip install xhs Pillow torch transformers
```

> 💡 **BLIP 图像识别可选**：如果只想用 API 发布（不需要 AI 识图），只需装 `xhs` 即可。

### 2. 获取 Cookie

> **关键步骤！必须用 Chrome 无痕窗口 (Ctrl+Shift+N) 操作！**

1. 打开 Chrome 无痕窗口，登录 [小红书创作者中心](https://creator.xiaohongshu.com)
2. 按 F12 → Application → Cookies → 全选复制
3. 粘贴到 `xhs_cookie.txt` 文件（一行完整字符串）

> 详细图解教程见 `references/cookie-extraction.md`

### 3. 发布第一篇笔记

```bash
python xhs_publish.py   --folder "./素材/今日穿搭"   --title "今日OOTD 被自己温柔到了～"   --desc "今天也是被自己治愈的一天"

#OOTD #今日穿搭 #治愈系日常"
```

### 4. 验证发布

发布成功的笔记会返回 ID，在浏览器打开：
```
https://www.xiaohongshu.com/discovery/item/{笔记ID}
```

---

## 📖 详细用法

### 命令行参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `--folder PATH` | 必填 | 素材图片文件夹路径 |
| `--title TEXT` | 可选 | 笔记标题（≤20字） |
| `--desc TEXT` | 可选 | 笔记正文 |
| `--topics JSON` | 可选 | 话题标签 JSON |
| `--idx INT` | 可选 | 文案模板索引 0-22 |
| `--dry-run` | 标志 | 测试模式，仅验证不发布 |
| `--no-mark` | 标志 | 发布后不标记文件夹 |

### 配合 AI Agent 使用

```python
from xhs import XhsClient
from xhs.help import sign

cookie = open('xhs_cookie.txt').read().strip()

def sign_wrapper(uri, data=None, a1="", web_session=""):
    return sign(uri, data, a1=a1)

client = XhsClient(cookie=cookie, timeout=20, sign=sign_wrapper)
me = client.get_self_info2()
print(f"当前账号: {me['nickname']}")
```

---

## 🖼️ BLIP 图像识别（可选）

如果你的 AI Agent 不支持多模态视觉，BLIP 可以本地识别图片内容：

```python
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img = Image.open("照片.png")
inputs = processor(img, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=50, num_beams=5)
caption = processor.decode(out[0], skip_special_tokens=True)
# -> "a woman in a white dress standing in front of a building"
```

首次运行下载 ~1GB 模型，后续即用即走。

---

## ⚠️ 重要注意事项

| 问题 | 严重度 | 解决方案 |
|------|--------|----------|
| Cookie 混用 | 致命 | 必须用 Chrome 无痕窗口登录 |
| web_session 缺失 | 致命 | 从 DevTools Application 面板复制 |
| sign 参数顺序 | 致命 | `sign(uri, data, a1=a1)` — a1 用关键字传参 |
| Cookie 过期 | 一般 | 几小时到几天，重新获取即可 |
| 标题超 20 字 | 一般 | 小红书建议 ≤20 字 |

---

## 📁 项目结构

```
xhs-post/
├── xhs_publish.py          # 核心发布脚本
├── requirements.txt        # Python 依赖
├── references/             # 参考文档
│   ├── cookie-extraction.md
│   ├── blip-image-captioning.md
│   ├── image-recognition.md
│   └── xhs-cookie-format.md
└── README.md
```

---

## 🤝 贡献者

**Dabao** — 全部代码 · 文档 · 维护

欢迎提 Issue 和 PR！

---

## 📄 许可证

MIT License — 自由使用，保留署名即可。

---

## ⭐ 支持项目

如果这个工具对你有帮助，请给个 Star ⭐

你的 Star 是我持续更新的动力 💪

🔗 **github.com/DaBaoAgent/xhs-post**
