import os
import filecmp

path = './problem3_files'
folders = os.listdir(path)
file_list = []

# 将各个文件夹里的文件取出放到一个列表中
def mergeFiles(folders):
	for folder in folders:
		folder_path = path + '/' + folder
		folder = os.listdir(folder_path)
		for file in folder:
			file = folder_path + '/' + file 
			file_list.append(file)

#将列表里的文件两两进行比较，相同的则删除一个
def cmp(file_list):
	for x in file_list:
		for y in file_list:
			if os.path.exists(x) and os.path.exists(y) and x!= y: # 注意这种比较方法，会把自己与自己比，因此用x!=y去掉这种情况
				if filecmp.cmp(x,y):
					print(y)
					os.remove(y)

mergeFiles(folders)
cmp(file_list)