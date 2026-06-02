"""
小红书 API 图文发布脚本 — 纯钩子版（标题零暴露）
使用 xhs 库纯 Python API，无需浏览器

用法:
  python xhs_publish.py           # 自动选第一个未发布子文件夹
  python xhs_publish.py 48        # 指定子文件夹编号
"""
import os, sys, random, json
os.environ['PYTHONUTF8'] = '1'
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from datetime import datetime
from xhs import XhsClient
from xhs.help import sign

# ================ 配置区 ================
COOKIE_FILE = os.path.expanduser(r"~\.hermes\data\xhs_cookie_latest.txt")
with open(COOKIE_FILE, encoding='utf-8') as f:
    COOKIE = f.read().strip()

def sign_wrapper(uri, data=None, a1="", web_session=""):
    return sign(uri, data, a1=a1)

ROOT = Path(r"D:\BaiduSyncdisk\8 本地推素材\@自动发图文素材库\大宝小红书")
EXCLUDE_KEYWORDS = ["已发(小红书)", "已发(抖音)", "已发(双平台)", "已发(三平台)", "已发"]

def find_available_folder(root, folder_num=None):
    if folder_num is not None:
        target = root / str(folder_num)
        if target.is_dir():
            if any(kw in target.name for kw in EXCLUDE_KEYWORDS):
                existing = [d.name for d in root.iterdir() if d.is_dir() and not any(kw in d.name for kw in EXCLUDE_KEYWORDS)]
                print(f"❌ 文件夹 {folder_num} 已标记已发")
                print(f"   可用文件夹: {existing}")
                sys.exit(1)
            return target
        else:
            print(f"❌ 文件夹 {folder_num} 不存在")
            sys.exit(1)
    dirs = sorted([d for d in root.iterdir() if d.is_dir()])
    for d in dirs:
        if not any(kw in d.name for kw in EXCLUDE_KEYWORDS):
            return d
    print("❌ 没有可用素材文件夹（全部已发）")
    sys.exit(1)

folder_num = sys.argv[1] if len(sys.argv) > 1 else None
FOLDER = find_available_folder(ROOT, folder_num)
files = sorted([str(f) for f in FOLDER.glob("*.png")] + [str(f) for f in FOLDER.glob("*.jpg")])

if not files:
    print(f"❌ 子文件夹 {FOLDER.name} 中没有图片")
    sys.exit(1)

# ================ 纯钩子标题池（零业务暴露） ================
TITLE_POOL = [
    # 悬念型
    "发现了一个好东西……😭",
    "苏州人才知道的宝藏地方",
    "闺蜜说我太会过日子了",
    "刷到就是缘分，点进来看",
    "一般人我不告诉他🤫",
    "在苏州待了3年才知道…",
    "大数据请把这篇推给需要的人",
    # 情绪型
    "看到那一刻我没忍住",
    "谁说便宜没好货？？打脸了",
    "后悔没早点知道系列😭",
    "我承认之前是我大声了",
    "用完之后我只想说一句话",
    # 反常识型
    "不用买！不用买！不用买！",
    "居然可以这样？？我白花了好多钱",
    "苏州这个价格是认真的吗…",
    "算了一笔账，果断放弃购买",
    "花小钱办大事，我悟了",
    # 场景型
    "带家人出门再也不愁了",
    "去了趟医院才知道这东西能…",
    "亲戚来苏州，一个电话搞定了",
    "临时急用，结果被这个救了一命",
    "第一次体验这种操作，惊了",
    # 社交证明型
    "被问爆了，链接放这了",
    "发了朋友圈被问疯了",
    "闺蜜追着我要这个😭",
    # 短平快
    "太香了！",
    "绝了！",
    "这个我真的忍不住要分享",
]

USED_TITLES_FILE = os.path.expanduser(r"~\.hermes\data\xhs_used_titles.json")

def pick_title():
    pool = list(TITLE_POOL)
    random.shuffle(pool)
    used = []
    if os.path.exists(USED_TITLES_FILE):
        try:
            with open(USED_TITLES_FILE, encoding='utf-8') as f:
                data = json.load(f)
                used = data.get("used", [])
        except Exception:
            pass
    fresh = [t for t in pool if t not in used]
    if fresh:
        title = fresh[0]
    else:
        title = pool[0]
        used = []
    used = [title] + [u for u in used if u != title]
    used = used[:20]
    with open(USED_TITLES_FILE, 'w', encoding='utf-8') as f:
        json.dump({"used": used, "last_updated": datetime.now().isoformat()}, f, ensure_ascii=False, indent=2)
    return title

TITLE = pick_title()

# 正文（不暴露品类，纯故事+悬念）
DESC = """真的忍不住要分享这个😭

之前家里遇到一个难题，临时需要一个东西，网上搜了一圈买的话要大几千，只用几天太不划算了。

后来朋友说苏州有工厂可以直接… 我半信半疑试了一下，真的好用到我想安利给所有人🔥

几个让我惊喜的点：
✅ 真的不贵，比想象的便宜太多
✅ 用几天算几天，灵活到哭
✅ 工厂直接出，没有乱七八糟的加价
✅ 一个电话就送到，巨快

特别适合这些情况👇
🩹 家里有人临时需要照顾
👵 带长辈出门走走
🏥 定期要去医院的时候
✈️ 亲戚朋友来玩临时用几天

苏州本地从园区到昆山都能用，通借通还超方便💯

📩 想知道具体是什么？评论区扣\"1\"我私你～

#苏州生活 #宝藏分享 #省钱小妙招 #好物推荐 #真实体验"""

# 标签（生活类，不暴露品类）
TOPICS = [{"name": "苏州生活"}, {"name": "宝藏分享"}, {"name": "省钱小妙招"}, {"name": "好物推荐"}, {"name": "真实体验"}]
# ========================================

print(f"📁 文件夹: {FOLDER}")
print(f"📷 图片: {len(files)}张")
for f in files:
    print(f"   - {Path(f).name}")

print(f"\n📝 标题: {TITLE}")
print(f"\n🚀 开始发布...")
client = XhsClient(cookie=COOKIE, timeout=60, sign=sign_wrapper)
result = client.create_image_note(
    title=TITLE, desc=DESC, files=files,
    topics=TOPICS, is_private=False
)

score = result.get('data', {}).get('score', '?')
note_id = result['id'] if 'id' in result else result.get('data', {}).get('id', '?')
print(f"✅ 小红书发布成功! 笔记ID: {note_id}  score: {score}")

new_name = f"{FOLDER.name}-已发(小红书)"
FOLDER.rename(FOLDER.parent / new_name)
print(f"✅ 已标记: {FOLDER.name} → {new_name}")
