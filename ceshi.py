import os
import re

# 替换为你的文件夹路径
folder = r'C:\Users\21160\Desktop\web-site\heilai\images\Deathnote\第三卷'

# 正则：匹配如 image_1.jpg 或其他类似格式
pattern = re.compile(r'(.*?)(\d+)(\.jpg)$', re.IGNORECASE)

for filename in os.listdir(folder):
    match = pattern.match(filename)
    if match:
        prefix, number, suffix = match.groups()
        new_number = f"{int(number):03d}"  # 转换为3位数字
        new_name = f"{prefix}{new_number}{suffix}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"✅ 重命名: {filename} -> {new_name}")
