# 三平台发布 — 已验证环境清单

> 2026-05-18 实战验证

## Python 环境

| 项目 | 路径/版本 |
|------|-----------|
| **系统 Python** | `C:\Users\xxx13\AppData\Local\Programs\Python\Python312\python.exe` |
| **Hermes .venv** | 精简版，无 pip。**所有 pip install 必须用系统 Python** |
| **pip 代理** | 公司网络需 `--proxy="" --trusted-host pypi.org --trusted-host files.pythonhosted.org` |

## 已安装关键包

```bash
# 验证命令
/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe -c "import xhs; print('xhs:', xhs.__version__)"
# → xhs: 0.2.13

/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe -c "import camoufox; print('camoufox:', camoufox.__version__)"
# → camoufox: 0.4.11

/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe -c "from playwright.sync_api import sync_playwright; print('playwright: available')"
# → playwright: 1.59.0

/c/Users/xxx13/AppData/Local/Programs/Python/Python312/python.exe -c "import browser_cookie3; print('browser-cookie3: available')"
# → browser-cookie3: 0.20.1
```

## 浏览器

| 项目 | 位置 |
|------|------|
| **Camoufox** | `C:\Users\xxx13\AppData\Local\Camoufox\camoufox\` |
| **Playwright Chromium** | Playwright 管理（`playwright install chromium`） |

## 登录态存储

| 平台 | 文件 | 格式 | 状态 |
|------|------|------|------|
| 小红书 | Cookie 字符串（内存） | 纯文本 | ✅ 已获取（2026-05-18） |
| 抖音 | `~/.hermes/browser-profiles/douyin_state.json` | Playwright storage_state | ✅ 已保存（44 cookies） |
| 闲鱼 | `~/.hermes/browser-profiles/xianyu_state.json` | Playwright storage_state | ⚠️ 旧版，需 Camoufox 重登 |

> **注意**：小红书的 `web_session` 必须在 `xhs.XhsClient(cookie=COOKIE)` 中传完整 Cookie 字符串，不是单独字段。

## 关键限制

| 限制 | 影响 |
|------|------|
| `execute_code` 无系统包 | 不能用 `execute_code` 运行 xhs/camoufox/playwright 代码 → 必须用 `terminal` |
| `browser_*` 无登录态 | Hermes browser 工具无法复用 Playwright storage_state → 抖音/闲鱼不能用 browser_* |
| DeepSeek 无多模态 | `browser_vision` 始终失败 → 截图只能 MEDIA: 给用户看 |
| Windows stdout 缓冲 | `terminal(background=true)` 输出不显示 → 脚本必须写日志文件 |
