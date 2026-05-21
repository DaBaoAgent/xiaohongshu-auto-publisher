# BLIP 图像识别 — 小红书文案生成

## 场景
当模型不支持 vision（如 deepseek-v4-pro），`vision_analyze`/`browser_vision` 均失败时，用 BLIP 本地 CPU 识别照片内容，生成中文文案。

## 环境
Windows 主机，系统 Python 3.12，已预装：
- `torch` 2.6.0+cu124
- `transformers` 5.6.0
- `PIL` (Pillow) 12.2.0

无需额外安装。

## 执行方式
⚠️ `execute_code` 沙箱无 transformers，必须通过 `subprocess.run()` 调用系统 Python。

```python
# Agent 端 (execute_code)
import subprocess
python = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe"
script = r"C:\Users\Administrator\.hermes\scripts\_blip_caption.py"
result = subprocess.run([python, script], capture_output=True, text=True, timeout=300)
```

## 模型
`Salesforce/blip-image-captioning-base` (~1GB)
- 首次下载 ~200秒，利用 HF 断点续传
- 缓存于 `~/.cache/huggingface/hub/models--Salesforce--blip-image-captioning-base/`
- 后续运行秒级加载

## 输出示例
```
FOLDER 1: "a woman sitting in a chair on a beach"
FOLDER 2: "a woman standing in front of a building"
FOLDER 3: "a woman standing next to a stone wall"
FOLDER 4: "a woman sitting at a desk with a laptop"
FOLDER 5: "a woman sitting on a bike in the rain"
FOLDER 6: "a woman sitting on a rock next to a river"
```

## 英文描述 → 中文文案映射
| BLIP 描述 | 场景理解 | 文案方向 |
|-----------|----------|----------|
| beach, chair | 海边度假 | 治愈系/夏日/度假穿搭 |
| building, standing | 城市街拍 | OOTD/街拍/citywalk |
| stone wall | 街头氛围 | 质感/真实日常/做自己 |
| desk, laptop | 咖啡厅/学习 | 独处/慢生活/治愈 |
| bike, rain | 雨天骑行 | 文艺/街头/任性 |
| rock, river | 河边自然 | 大自然/治愈/慢生活 |
