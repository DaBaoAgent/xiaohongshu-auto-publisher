# 小红书 Cookie 管理

> 小红书 web_session 有效期约1-3天，过期后需手动重新获取。

## 过期症状

xhs API 返回：
```json
{"code": -100, "msg": "无登录信息"}
```

## 获取新 Cookie（2分钟）

1. Chrome 打开 `https://creator.xiaohongshu.com`
2. 手机号 + 验证码登录
3. F12 → Application → Cookies → `www.xiaohongshu.com`
4. 复制完整 Cookie 字符串（重点：`web_session`、`a1`、`webId`、`websectiga`、`sec_poison_id`）
5. 确认 `xsecappid` = `xhs-pc-web`

## 保存位置

将完整 Cookie 写入 `~/.hermes/data/xhs_cookie_latest.txt`（一行，无需精简）：
```bash
echo "你的完整Cookie字符串" > ~/.hermes/data/xhs_cookie_latest.txt
```

## 🔴 Cookie 模板陷阱（2026-05-25 修复）

**历史问题**：`xhs_publish.py` 模板脚本硬编码 `COOKIE = "你的完整Cookie字符串"`。cron agent 复制模板生成 `pub_xhs_N.py` 时填入过期值，导致连续3次静默失败（cron 报 ok 但实际 `code: -100`）。

**修复（v3.3.0）**：模板改为动态读取：
```python
# ✅ 修改后：每次运行前从文件读取最新 Cookie
COOKIE_FILE = os.path.expanduser(r"~\.hermes\data\xhs_cookie_latest.txt")
with open(COOKIE_FILE, encoding='utf-8') as f:
    COOKIE = f.read().strip()
```

**效果**：用户只需更新 `~/.hermes/data/xhs_cookie_latest.txt`，cron 下次触发自动使用新 Cookie，无需修改任何脚本。

## 保存位置

将完整 Cookie 写入 `~/.hermes/data/xhs_cookie_latest.txt`（一行，无需精简）：
```bash
echo "你的完整Cookie字符串" > ~/.hermes/data/xhs_cookie_latest.txt
```

## 发布脚本 Cookie 读取

所有发布脚本统一从此文件读取：
```python
COOKIE_FILE = os.path.expanduser(r"~\.hermes\data\xhs_cookie_latest.txt")
with open(COOKIE_FILE, encoding='utf-8') as f:
    COOKIE = f.read().strip()
```

## 验证 Cookie 有效性

```bash
python -c "
import os
cookie_file = os.path.expanduser(r'~\.hermes\data\xhs_cookie_latest.txt')
with open(cookie_file) as f:
    cookie = f.read().strip()
print(f'长度: {len(cookie)}, 含web_session: {\"web_session\" in cookie}')
"
```
