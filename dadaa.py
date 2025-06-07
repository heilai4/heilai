import os
import json

chapter_folder = 'images/Deathnote/第二卷'
pages = sorted(os.listdir(chapter_folder))  # 获取排序后的文件列表

data = {
    "title": "死亡笔记",
    "chapters": [
        {
            "id": "chapter1",
            "title": "第2话",
            "pages": pages
        }
        # 你可以多章节重复类似操作
    ]
}

with open('comic.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
