#!/usr/bin/env python3
r"""
小红书发布脚本 - 粥玲丽 22岁女孩日常分享
v4.0 2026-05-21

用法:
  python xhs_publish.py --folder "D:\BaiduSyncdisk\17 新小红书\出图\1" --title "..." --desc "..."

环境变量:
  XHS_FOLDER  - 素材文件夹路径
  XHS_TITLE   - 笔记标题
  XHS_DESC    - 笔记正文
  XHS_TOPICS  - JSON话题列表
  XHS_DRY_RUN - 1=仅验证不发布
"""

import os, sys, json, argparse
os.environ['PYTHONUTF8'] = '1'
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from xhs import XhsClient
from xhs.help import sign

SCRIPT_DIR = Path(__file__).parent
COOKIE_FILE = SCRIPT_DIR / "xhs_cookie.txt"
DEFAULT_ROOT = Path(r"D:\BaiduSyncdisk\17 新小红书\出图")

# ============================================================
# 22岁女孩小红书审美 - 文案模板
# ============================================================

TITLE_TEMPLATES = [
    "今日OOTD 被自己温柔到了～",
    "22岁的快乐 就是穿上喜欢的小裙子",
    "早八人也要精致出门呀",
    "今天穿这样去约会会被夸吗",
    "夏天就要穿得清清爽爽",
    "新买的这件也太好看了吧！！",
    "姐妹们帮我看看这套搭不搭",
    "平淡日子里的小确幸",
    "和姐妹的快乐周末",
    "记录生活里最真实的样子",
    "普通女孩的日常碎片",
    "最近的生活也太美好了吧",
    "咔嚓咔嚓 留下今天的自己",
    "今天也是元气满满的一天呀",
    "氛围感拿捏住了",
    "这个光线也太温柔了吧",
    "阳光正好 我也正好",
    "是夏天傍晚的感觉了",
    "治愈系日常",
    "被生活温柔以待的一天",
    "希望你今天也开心呀",
    "所有美好都值得被记录",
    "今天的心情是粉色的",
]

DESC_TEMPLATES = [
    "今天也是被自己治愈的一天呀～\n\n天气好好 心情也好好\n穿了最近最喜欢的这套出门\n每个角度都想记录下来\n\n希望看到这条的你\n今天也会有好心情呀\n\n#OOTD #日常穿搭 #夏日穿搭 #氛围感 #记录生活 #治愈系 #22岁\n#ootd #lookoftheday",

    "记录一下今天的日常碎片\n\n没有什么特别的\n但就是觉得很幸福\n阳光 微风 喜欢的衣服\n还有好心情\n\n生活中的小确幸\n都值得被看见呀\n\n#日常生活碎片 #我的日常 #治愈系日常 #氛围感 #记录生活 #快乐日常\n#dailylife #cozyvibes",

    "姐妹们！！\n这件真的太好看了吧\n\n本来只是随便试试\n结果穿上就脱不下来了\n质感超级好 颜色也好温柔\n22岁就要穿得漂漂亮亮的呀\n\n你们觉得怎么样～\n评论区告诉我\n\n#OOTD #穿搭分享 #温柔系穿搭 #夏日穿搭 #女生穿搭 #质感穿搭\n#outfitinspo #style",

    "咔嚓\n今天的阳光和心情都刚刚好～\n\n22岁 平凡又美好的年纪\n想记录下每一个美好的瞬间\n不管是穿什么 在哪里\n只要开心就好呀\n\n愿我们都能被生活温柔以待\n\n#氛围感 #记录生活 #治愈系 #温柔日常 #生活碎片 #拍照姿势\n#aesthetic #mood",

    "夏天就是最好的滤镜呀\n\n光线好的时候 忍不住多拍几张\n今天选了好久的look\n出门就被姐妹夸了嘻嘻\n女孩子的快乐就是这么简单\n\n你们的夏天都穿什么呀～\n快来评论区分享\n\n#夏日穿搭 #OOTD #轻熟风 #温柔穿搭 #夏天来了 #女生日常\n#summervibes #outfit",

    "这是一份不完美的日常\n\n没有刻意摆拍\n没有精心设计\n就是最真实的我呀\n22岁 还在学着爱自己\n学着接纳每一个瞬间\n\n真实的你 就很美\n\n#真实日常 #拒绝容貌焦虑 #做自己 #治愈系 #日常记录 #慢生活\n#selflove #reallife",
]

TOPIC_POOLS = {
    "ootd": [
        {"name": "OOTD"}, {"name": "今日穿搭"}, {"name": "温柔系穿搭"},
        {"name": "夏日穿搭"}, {"name": "日常穿搭"}, {"name": "女生穿搭"},
        {"name": "质感穿搭"}, {"name": "ootd"}, {"name": "穿搭灵感"},
    ],
    "life": [
        {"name": "日常生活碎片"}, {"name": "记录生活"}, {"name": "治愈系日常"},
        {"name": "氛围感"}, {"name": "生活碎片"}, {"name": "慢生活"},
        {"name": "快乐日常"}, {"name": "温柔日常"},
    ],
    "mood": [
        {"name": "治愈系"}, {"name": "做自己"}, {"name": "好心情"},
        {"name": "自我成长"}, {"name": "爱自己"}, {"name": "女性成长"},
    ],
    "photo": [
        {"name": "拍照姿势"}, {"name": "氛围感拍照"}, {"name": "手机摄影"},
        {"name": "日常拍照"}, {"name": "aesthetic"},
    ],
    "season": [
        {"name": "夏天来了"}, {"name": "初夏"}, {"name": "summervibes"},
        {"name": "夏日限定"},
    ],
}


def pick_by_idx(seq, idx=0):
    return seq[idx % len(seq)]


def load_cookie():
    if COOKIE_FILE.exists():
        cookie = COOKIE_FILE.read_text(encoding='utf-8').strip()
        if cookie:
            return cookie
    print(f"ERROR: Cookie file missing: {COOKIE_FILE}")
    sys.exit(1)


def sign_wrapper(uri, data=None, a1="", web_session=""):
    return sign(uri, data, a1=a1)


def get_images(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print(f"ERROR: Folder not found: {folder}")
        sys.exit(1)
    exts = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'}
    files = sorted([
        str(f) for f in folder.iterdir()
        if f.suffix.lower() in exts
    ])
    if not files:
        print(f"ERROR: No images in: {folder}")
        sys.exit(1)
    return files


def publish(folder, title, desc, topics, dry_run=False):
    cookie = load_cookie()
    files = get_images(folder)
    
    print(f"IMAGES: {len(files)}")
    for f in files:
        print(f"  {Path(f).name}")
    
    if dry_run:
        print("MODE: DRY_RUN - skipping publish")
        return {"id": "dry_run", "status": "skipped"}
    
    print(f"TITLE: {title}")
    print(f"TOPICS: {[t['name'] for t in topics]}")
    print("PUBLISHING...")
    
    client = XhsClient(cookie=cookie, timeout=60, sign=sign_wrapper)
    result = client.create_image_note(
        title=title, desc=desc, files=files,
        topics=topics, is_private=False
    )
    note_id = result.get('id', '???')
    print(f"SUCCESS: {note_id}")
    print(f"URL: https://www.xiaohongshu.com/discovery/item/{note_id}")
    return result


def mark_published(folder_path):
    folder = Path(folder_path)
    new_name = f"{folder.name}-已发(小红书)"
    new_path = folder.parent / new_name
    if new_path.exists():
        print(f"SKIP: {new_name} already exists")
        return
    folder.rename(new_path)
    print(f"MARKED: {folder.name} -> {new_name}")


def main():
    parser = argparse.ArgumentParser(description="XHS Publish - Zhou Lingli")
    parser.add_argument("--folder", help="素材文件夹路径")
    parser.add_argument("--title", help="笔记标题")
    parser.add_argument("--desc", help="笔记正文")
    parser.add_argument("--topics", help="JSON话题列表")
    parser.add_argument("--dry-run", action="store_true", help="测试模式")
    parser.add_argument("--no-mark", action="store_true", help="不标记已发")
    parser.add_argument("--idx", type=int, default=0, help="文案模板索引")
    args = parser.parse_args()
    
    folder = args.folder or os.environ.get("XHS_FOLDER")
    title = args.title or os.environ.get("XHS_TITLE")
    desc = args.desc or os.environ.get("XHS_DESC")
    topics_raw = args.topics or os.environ.get("XHS_TOPICS")
    dry_run = args.dry_run or os.environ.get("XHS_DRY_RUN") == "1"
    
    # auto-select folder
    if not folder:
        root = DEFAULT_ROOT
        dirs = sorted([d for d in root.iterdir() if d.is_dir() and "已发" not in d.name])
        if not dirs:
            print("ALL_DONE: no unpublished folders")
            sys.exit(0)
        folder = str(dirs[0])
        print(f"AUTO_FOLDER: {dirs[0].name}")
    
    # auto-generate
    if not title:
        title = pick_by_idx(TITLE_TEMPLATES, args.idx)
        print(f"AUTO_TITLE: {title}")
    if not desc:
        desc = pick_by_idx(DESC_TEMPLATES, args.idx)
        print(f"AUTO_DESC: yes")
    
    if not topics_raw:
        all_t = []
        for pool in TOPIC_POOLS.values():
            all_t.extend(pool)
        topics = [all_t[i % len(all_t)] for i in range(args.idx, args.idx + 5)]
    else:
        topics = json.loads(topics_raw)
    
    result = publish(folder, title, desc, topics, dry_run)
    
    if not dry_run and not args.no_mark:
        mark_published(folder)
    
    print(f"RESULT_JSON: {json.dumps(result, ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
