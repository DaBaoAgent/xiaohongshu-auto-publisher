# 小红书 Cookie 提取方法（已验证）

> 2026-05-21 实战验证。问题：用户普通Chrome窗口已登录3个轮椅账号，多次提取Cookie均为错误账号。

## 正确方法：Chrome 无痕窗口

### 步骤

1. **打开无痕窗口**：Chrome → `Ctrl+Shift+N`（或菜单→新建无痕窗口）
2. **访问 xiaohongshu.com**，点击登录
3. **用粥玲丽账号登录**（小红书号 95830384200）
4. **登录成功后**，按 `F12` 打开 DevTools
5. **Application → Cookies → www.xiaohongshu.com**
6. **全选所有 Cookie**（Ctrl+A），复制完整列表
7. 粘贴给 Agent，Agent 会自动格式化为 `key=value; key2=value2` 字符串

### 为什么必须无痕窗口

| 普通窗口 | 无痕窗口 |
|----------|----------|
| 3个轮椅账号Cookie共存 | 隔离环境，零污染 |
| `document.cookie` 混入多个账号 | 只有当前登录账号 |
| web_session 始终是轮椅账号的 | web_session 是目标账号的 |

### Cookie 格式转换

Chrome DevTools 导出的表格格式：
```
a1  19e48f7b...  .xiaohongshu.com  /  2027-05-21...
web_session  040069b8...  .xiaohongshu.com  /  ...
```

Agent 自动转换为：
```
a1=19e48f7b...; web_session=040069b8...; ...
```

### 验证 Cookie 归属

保存后立即验证：
```python
from xhs import XhsClient
from xhs.help import sign

cookie = open('scripts/xhs_cookie.txt').read().strip()
client = XhsClient(cookie=cookie, timeout=20, 
    sign=lambda uri,data=None,a1='',web_session='': sign(uri,data,a1=a1))
me = client.get_self_info2()

# 期望输出 nickname='粥玲丽', red_id='95830384200'
# 如果输出 '昆山工厂轮椅直租' → Cookie污染，重新无痕窗口提取
```

### 已知轮椅账号（不要用）

| 账号 | web_session 前缀 | red_id |
|------|-----------------|--------|
| 昆山工厂轮椅直租 | `040069b6b6eae...` | 95480619590 |
| 其他轮椅账号 | — | — |
