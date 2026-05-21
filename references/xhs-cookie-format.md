# 小红书 xhs 库 Cookie 格式（2026-05-18 验证通过）

## 已验证可用的 Cookie 结构

从 DevTools Application → Cookies → `www.xiaohongshu.com` 复制完整 Cookie 字符串。

**必需字段（缺一不可）：**

| Cookie 字段 | 用途 | 获取方式 |
|-------------|------|----------|
| `a1` | 签名算法核心参数 | DevTools Application 面板 |
| `webId` | 设备标识 | DevTools Application 面板 |
| `web_session` | **登录凭证核心** (HttpOnly) | DevTools Application 面板 |
| `websectiga` | 安全令牌 | DevTools Application 面板 |
| `sec_poison_id` | 反爬指纹 | DevTools Application 面板 |

**可选字段（增加无妨）：**
`abRequestId`, `acw_tc`, `ets`, `webBuild`, `xsecappid`, `loadts`, `id_token`, `unread`, `x-rednote-datactry`, `x-rednote-holderctry`

**格式：** 分号分隔的 `key=value` 对，例如：
```
a1=19e3ae337b0...; webId=89a335bda1c...; web_session=040069b6894b...; websectiga=59d3ef1e60c...; sec_poison_id=fee75bbc-dabd-...
```

## ⚠️ 常见错误

| 错误现象 | 根因 |
|----------|------|
| `document.cookie` 取不到 `web_session` | HttpOnly Cookie，必须 DevTools 手动复制 |
| 返回"无登录信息" | `web_session` 缺失或过期 |
| `ValueError` 签名错误 | `a1` 传参顺序错误，必须 keyword: `sign(uri, data, a1=a1)` |

## 获取流程

1. 浏览器打开 `https://creator.xiaohongshu.com`
2. **确保已登录**（看到创作者中心首页）
3. F12 → Application → Storage → Cookies → `www.xiaohongshu.com`
4. 逐个复制上述必需字段的值
5. 拼接为 `key1=value1; key2=value2; ...` 格式
