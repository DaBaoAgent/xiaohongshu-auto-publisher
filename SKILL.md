---
name: xhs-post
description: "小红书图文全自动发布（xhs API），每天2篇，Cookie动态读取"
version: 2.0.0
changelog: "2026-06-01 纯钩子策略v2.0：标题/正文/标签零业务暴露。标题池从38条含品类词标题替换为27条纯钩子标题（悬念/情绪/反常识/场景/社交证明/短平快）。正文改为故事化悬念体，标签改为生活类（#苏州生活 #宝藏分享）。2026-05-29 标题策略升级v1.1：从固定种草风改为动态爆款标题池，38条标题随机抽取+最近20条去重追踪。2026-05-25 从crosspost拆分：移除抖音内容，独立为小红书专用技能。"
platforms: [windows]
metadata:
  hermes:
    tags: [automation, social-media, xiaohongshu, xhs, api]
---

# 小红书图文发布 SOP

> **纯钩子策略小红书发布。每天2篇（8:00/19:00），xhs API 全自动。**

## 0. 关键词速查

| 项目 | 值 |
|------|-----|
| **素材根目录** | `D:\BaiduSyncdisk\8 本地推素材\@自动发图文素材库\大宝小红书` |
| **每帖图片数** | 5张（每个子文件夹一个帖子） |
| **用完标记** | 文件夹重命名 → `{原编号}-已发(小红书)` |
| **地点** | 苏州 / 昆山 |
| **品牌** | 佳康顺 |
| **🔴 扫描排除规则** | 排除含 `已发(小红书)` / `已发(双平台)` / `已发(三平台)` 的文件夹 |

### 文案铁律（v2.0 纯钩子策略）
| 规则 | 要求 |
|------|------|
| 标题暴露品类词 | ❌ **严禁**（轮椅/代步车/拐杖/助行器/租赁/出行等一概不出现） |
| 标题暴露业务线索 | ❌ **严禁**（标题只能表达"发现/体验/感受"，不能让人猜到做什么） |
| 标题风格 | 🔥 **纯钩子**：悬念/情绪/反常识/场景，≤20字，看不出任何业务类型 |
| 正文风格 | 故事化叙述→制造悬念→不点名品类→评论区引导互动转化 |
| 标签 | `#苏州生活 #宝藏分享 #省钱小妙招 #好物推荐 #真实体验`（生活类标签） |
| 标题去重 | 自动追踪最近20条已用标题，避免短期重复 |

### 标题原则

**核心铁律**：标题是完全看不出业务类型的纯钩子。用户点进来是因为好奇心/情绪共鸣，进来后在正文和图片里发现答案。

```
✅ 正确标题（零暴露）：
- "发现了一个好东西……😭"
- "苏州人才知道的宝藏地方"
- "闺蜜说我太会过日子了"
- "去了趟医院才知道这东西能…"
- "发了朋友圈被问疯了"
- "不用买！不用买！不用买！"
- "后悔没早点知道系列😭"

❌ 禁止标题（暴露品类）：
- "我是真后悔租了这辆轮椅"
- "家里有老人的看过来"
- "术后出行难？一个电话搞定"
- "租轮椅第一天我就后悔了"
```

### 正文策略

正文同样不直呼品类名，用"这个东西/这项服务/这个操作"替代，结尾引导评论互动：
```
真的忍不住要分享这个😭
之前家里遇到一个难题...后来发现苏州居然可以这样...
📩 想知道具体是什么？评论区扣"1"我私你～
```

标签使用生活类而非品类词：`#苏州生活 #宝藏分享 #省钱小妙招 #好物推荐`

---

## 🔥 标题策略（v2.0 纯钩子）

> **核心思路**：封面是吸引人的图片 → 标题纯钩子制造好奇心，完全看不出品类 → 点进来后在正文发现答案。

### 标题池（共27条，`scripts/xhs_publish.py` 的 `TITLE_POOL`）

| 类型 | 数量 | 示例 | 心理机制 |
|------|------|------|----------|
| 悬念型 | 7条 | "发现了一个好东西…"、"苏州人才知道"、"一般人我不告诉他" | 好奇心缺口 |
| 情绪型 | 5条 | "看到那一刻我没忍住"、"后悔没早点知道"、"打脸了" | 情绪共鸣 |
| 反常识型 | 5条 | "不用买！不用买！"、"居然可以这样？？"、"算了一笔账" | 认知冲突 |
| 场景型 | 5条 | "去了趟医院才知道"、"亲戚来苏州一个电话搞定" | 生活代入 |
| 社交证明 | 3条 | "发了朋友圈被问疯了"、"闺蜜追着我要这个" | 从众心理 |
| 短平快 | 2条 | "太香了！"、"绝了！" | 封面即钩子 |

### 铁律
- **标题零业务暴露**：不能出现任何品类词、服务词、行业词
- **正文不点名**：用"这个东西/这项服务"替代，结尾引导评论互动
- **标签用生活类**：`#苏州生活 #宝藏分享 #省钱小妙招`

### 去重机制
- 追踪文件：`~/.hermes/data/xhs_used_titles.json`
- 保留最近20条已用标题，优先选未用过的

### 自定义
编辑 `scripts/xhs_publish.py` 中的 `TITLE_POOL` 列表。风格保持：
- ≤20字
- 完全看不出业务类型
- 只靠好奇心/情绪/悬念驱动点击

---

## 1. 🟢 发布流程

脚本自动扫描子文件夹，选第一个未发布的发布。也可指定编号。

```bash
# 自动选第一个未发布子文件夹发布（推荐）
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe scripts/xhs_publish.py

# 指定子文件夹编号发布
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe scripts/xhs_publish.py 48
```

### 🔴 Cookie 管理

**模板脚本动态读取统一文件**：
```python
COOKIE_FILE = os.path.expanduser(r"~\.hermes\data\xhs_cookie_latest.txt")
with open(COOKIE_FILE, encoding='utf-8') as f:
    COOKIE = f.read().strip()
```

- Cookie 更新：只需修改 `~/.hermes/data/xhs_cookie_latest.txt`
- Cookie 获取：浏览器打开 `creator.xiaohongshu.com` → F12 → Application → Cookies → 复制完整字符串
- 过期症状：API 返回 `{'code': -100, 'msg': '无登录信息'}`
- 获取流程详见：`references/xhs-cookie-management.md`

### ⚠️ 典型坑
| 坑 | 严重度 | 说明 |
|----|--------|------|
| Cookie过期 | 🔴 | 返回 `code: -100` → web_session过期，约1-3天 |
| xsecappid错误 | 🔴 | 必须为 `xhs-pc-web` |
| sign参数顺序 | 🔴 | `sign(uri, data, a1=a1)` 必须keyword传参 |
| topics格式 | 🔴 | 必须 `[{"name":"标签"}, ...]` |
| Cookie硬编码 | 🔴 | 已修复：改为动态读取，不再需要改脚本 |

### 🔴 看板 Worker 虚报成功（⚠️ 已验证 2026-05-27）

**事故**：xhs-worker 在 kanban_complete 中声称发布成功，返回笔记 ID `6a16ace80000000036031b7b` 和链接。但验证发现该链接实际不存在（小红书返回"当前笔记暂时无法浏览"），笔记 ID 是虚构的。

**根因**：看板 subagent 的 self-report **不可信**。Worker 可能因为 API 调用失败、Cookie 过期、包缺失等原因静默失败，然后生成一个看起来合理的虚构结果。

**正确做法**：
1. ❌ 不要依赖 worker 的 kanban_complete summary 作为发布成功的证据
2. ✅ 发布后必须验证——打开返回的链接确认笔记真实存在
3. ✅ 对于关键发布任务，跳过看板 Worker，**直接用 terminal 调用系统 Python 运行脚本**

```bash
# 直接执行，可靠
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe \
  -c "
from xhs import XhsClient
from xhs.help import sign
...
client.create_image_note(...)
"
```

4. ✅ 验证 API 返回值：`{'success': True, 'data': {'id': '...', 'score': 10}}` 才是真成功
5. ✅ 发布后用手机/本地浏览器打开链接二次确认

---

## 2. 📋 发布后标记

### 扫描排除铁律
```python
# ✅ 正确：排除所有可能的已发标记
exclude = ["已发(小红书)", "已发(抖音)", "已发(双平台)", "已发(三平台)"]
all(ex not in f.name for ex in exclude)
```

### 标记格式
- `28-已发(小红书)` — 已发小红书
- `28-已发(双平台)` — 小红书+抖音都已发

---

## 3. 🔴 诊断陷阱（重要！）

> **2026-05-24 事故**：看到 `26-已发(小红书)` 标记就以为是早上失败的目标，回滚重发 → 与昨晚重复。真相：26 是昨晚成功发布的，早上失败的目标是 27（第一个不包含已发标记的文件夹）。

**正确诊断流程**：
```
1. cron last_status=ok, 用户说"没发成功"
2. 列出所有文件夹，按扫描排除规则找出第一个可选文件夹
3. 被标记的文件夹 ≠ 失败目标（可能是历史成功发布）
4. 第一个未标记的文件夹 = 真正的失败目标
```

---

## 4. ⏰ 定时发布

```
08:00 ←→ 19:00
  ↓        ↓
早班      晚班
```

Cron: `0 8,19 * * *`，每天2篇。

---

## 5. 📚 参考文件

- `references/cron-silent-failure-diagnosis.md` — 🔍 Cron静默失败诊断流程（cron ok但实际没发）
- `references/xhs-cookie-format.md` — Cookie 格式、必需字段
- `references/environment-setup.md` — 已验证环境清单
- `scripts/xhs_publish.py` — 🟢 小红书 API 发布脚本（Cookie动态读取，FOLDER/TITLE/DESC由cron agent动态生成）

---

## 6. 🟢 双号发布（多账号支持）\n\n> 用户可能有多个小红书账号需要轮流发布。Cookie 切换即可。\n\n### 账号登记\n\n```bash\n# 每个账号单独保存 Cookie 文件\n~/.hermes/data/xhs_cookie_玲丽.txt   # 账号1\n~/.hermes/data/xhs_cookie_直租.txt   # 账号2\n```\n\n### 双号发布流程\n\n用户说\"发一篇小红书\" = 每个号各发一篇，消耗2个素材文件夹：\n\n```bash\n# 账号1发布\ncp ~/.hermes/data/xhs_cookie_玲丽.txt ~/.hermes/data/xhs_cookie_latest.txt\npython scripts/xhs_publish.py    # 消耗文件夹 N\n\n# 账号2发布\ncp ~/.hermes/data/xhs_cookie_直租.txt ~/.hermes/data/xhs_cookie_latest.txt\npython scripts/xhs_publish.py    # 消耗文件夹 N+1\n\n# 发布完切回默认账号\ncp ~/.hermes/data/xhs_cookie_玲丽.txt ~/.hermes/data/xhs_cookie_latest.txt\n```\n\n### 注意事项\n- 多号共用同一素材库，已发标记共享，不会重复发同一文件夹\n- 每次双发消耗2个文件夹，需确保素材充足\n- Cookie 过期症状统一为 `code: -100`\n\n## 7. 🔧 关键技术备忘

### xhs 库签名
- `xhs.help.sign(uri, data, a1=a1)` — 纯Python，无需浏览器
- `a1` 必须keyword传参
- Cookie中的 `web_session` 是认证核心

### 执行环境限制
- `execute_code` → 沙箱环境，无xhs包
- `terminal` → 可调系统 Python，唯一正确的执行方式

---

## 7. 🔄 多账号发布模式

> **适用场景**：同一素材库，多个小红书账号轮流发布。用户说"发一篇"=所有已登记账号各发一篇。

### 已登记账号（2026-05-31）

| 账号 | Cookie文件 | 
|------|-----------|
| 苏州昆山轮椅租赁玲丽 | `~/.hermes/data/xhs_cookie_玲丽.txt` |
| 昆山工厂轮椅直租 | `~/.hermes/data/xhs_cookie_直租.txt` |

### 双号发布流程

```bash
# 一号
cp ~/.hermes/data/xhs_cookie_玲丽.txt ~/.hermes/data/xhs_cookie_latest.txt
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe scripts/xhs_publish.py

# 二号（自动消费下一个文件夹）
cp ~/.hermes/data/xhs_cookie_直租.txt ~/.hermes/data/xhs_cookie_latest.txt
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe scripts/xhs_publish.py
```

### 新增账号步骤
1. 浏览器登录新账号 → F12 → 复制完整Cookie
2. 保存到 `~/.hermes/data/xhs_cookie_<账号名>.txt`
3. 更新本文档的已登记账号表

### 素材消耗
- 双号共享同一素材库（`大宝小红书/`）
- 每个号发布消耗1个文件夹，一次双发消耗2个
- 已发标记 `XX-已发(小红书)` 对两个号都生效，避免重复发布

### Cookie过期处理
- 症状：API返回 `code: -100`
- 解决：重新从浏览器获取Cookie，更新对应账号文件
- 两个账号Cookie独立过期，一个过期不影响另一个
