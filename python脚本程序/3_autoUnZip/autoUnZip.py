import os 
import shutil

"""
自动扫描压缩包并解压，然后删除压缩包

"""

def scanf():
	files = os.listdir()
	for f in files:
		if f.endswith('zip'):
			return f

def un_zip(f):
	path = f.split('.')[0]
	target_path = './' + path
	# os.mkdir(target_path)
	shutil.unpack_archive(f, target_path)

def delete(f):
	os.remove(f)

while True:
	f = scanf()
	if f:
		un_zip(f)
		delete(f)