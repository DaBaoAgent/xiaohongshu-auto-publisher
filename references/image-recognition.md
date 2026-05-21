# 图像识别方案 — BLIP 模型

> crosspost v4.0 配套。当 Agent 模型不支持多模态视觉时，用 BLIP 做本地图像描述。

## 方案选择

| 方案 | 可行 | 说明 |
|------|------|------|
| vision_analyze 工具 | ❌ | deepseek-v4-pro 不支持多模态 |
| browser_vision | ❌ | 同上，底层模型限制 |
| 色彩分析(PIL) | ❌ | 太粗糙，只能判断亮度/色调，无法描述内容 |
| **BLIP 模型(Python)** | ✅ | 纯本地，~1GB模型，CPU可跑，英文描述 |

## 依赖

系统 Python 需安装（本机已有）:
```
torch >= 2.0
transformers >= 4.x
Pillow
```

## 使用代码

```python
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 首次运行自动下载 ~1GB 模型到 ~/.cache/huggingface/
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 识别单张图片
img = Image.open("photo.png")
inputs = processor(img, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=50, num_beams=5)
caption = processor.decode(out[0], skip_special_tokens=True)
print(caption)  # 英文描述，如 "a woman sitting in a chair on a beach"
```

## Agent 工作流集成

1. 用 `execute_code` + `subprocess.run()` 调用系统 Python 执行 BLIP 脚本
2. 识别每组的代表性图片（建议每文件夹第一张）
3. 基于英文描述 + 人设（22岁女孩）生成中文文案
4. 文案审批后发布

## 性能

- 模型下载：首次 ~200秒（1GB，断点续传）
- 单张识别：~1-2秒（CPU）
- 6组识别：~10秒

## 注意事项

- 描述是英文的，需要 Agent 翻译并适配小红书中文文案风格
- 模型输出较简短（一句话），不会描述服装细节——Agent 需根据场景类型（户外/室内/城市/自然）补充细节
- 批次处理时建议逐张处理，避免内存溢出
