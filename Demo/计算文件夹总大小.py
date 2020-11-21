# 使用walk计算文件夹总大小
import os
d = os.walk(r'C:\Users\Ivan\python_learning_notes\Demo')
size = 0

for i in d:
    path, dir_list, name_list = i
    for name in name_list:
        abs_path = os.path.join(path, name)
        size += os.path.getsize(abs_path)

print(size)
