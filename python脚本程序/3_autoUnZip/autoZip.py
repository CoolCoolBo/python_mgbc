# coding:utf-8
from shutil import make_archive
import os
import time
# 指定需要监测的文件夹
image_path = './image'
# 指定压缩包存放的文件夹
output_path = './output'
# 记录生成了多少个压缩包
zip_count = 0
# 利用while True使程序持续运行
while True:
    files = os.listdir(image_path)
    # files变量中存储了路径下所有文件的文件名，len()函数可以获取list变量包含多少个元素
    # files_count即为路径下的文件数
    files_count = len(files)
    if files_count >= 5:
        zip_count = zip_count + 1
        # 指定压缩包的名称以及路径
        zip_name =  output_path + '/' + 'archive' + str(zip_count) 
        # 压缩文件
        make_archive(zip_name, 'zip', image_path)
        # 删除压缩过的文件
        for f in files:
            os.remove(image_path + '/' + f)
    # 休眠1秒，达到每1秒监测一次的效果
    time.sleep(1)