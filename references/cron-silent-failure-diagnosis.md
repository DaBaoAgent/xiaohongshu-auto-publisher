# Cron 静默失败诊断流程

> 适用：cron `last_status: ok`，用户反馈"没发成功"

## 诊断步骤

### 1. 找到 cron session
```bash
session_search(limit=10, sort="newest")
```
Session 格式：`cron_{job_id前12位}_{YYYYMMDD}_{HHMMSS}`

### 2. 搜索关键模式
```bash
search_files(pattern="code.*-100|无登录信息|发布成功|SILENT",
  file_glob="*{session_id}*", path="~/.hermes/sessions/")
```

### 3. 判读结果

| 匹配 | 含义 | 修复 |
|------|------|------|
| `code: -100, 无登录信息` | Cookie过期 | 更新 `xhs_cookie_latest.txt` |
| `发布成功` + 笔记ID | 真的成了 | 把链接发用户 |
| `SILENT` | 成功但静默 | 检查文件夹是否被标记 |

### 4. 读结论
```bash
read_file("session_{id}.json", offset=total_lines-70)
```
看 agent 最终的 stop 消息。

## ❌ 诊断陷阱

```
看到 26-已发(小红书) → 以为26是失败目标 → 回滚重发 → 重复！
正确：按排除规则找第一个未标记文件夹 → 那才是失败目标
```

## 历史案例

| 日期 | 症状 | 根因 |
|------|------|------|
| 5/25 08:02 | xhs-post ok，没发 | Cookie硬编码占位符→API code:-100 |
| 5/24 08:03 | xhs-post ok，没发 | web_session过期 |
| 5/24 14:00 | xianyu-post 超时 | Z盘网络断连（已迁移D盘） |
