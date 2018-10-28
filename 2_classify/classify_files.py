import os
import shutil

"""
将files里面的文件分别归类

"""
path = './files'
files = os.listdir(path)

for f in files:
	foldPath = os.path.join(path, f.split('.')[-1])
	file = os.path.join(path, f)
	if os.path.exists(foldPath):
		shutil.move(file, foldPath)
	else:
		os.makedirs(foldPath)
		shutil.move(file, foldPath)