import os
import shutil

path = './images'
files = os.listdir(path)
file_list = []
count = 0

for f in files:
	file_list.append(f)
	if len(file_list) == 5:
		count += 1
		zipPath = path + '/' + 'archive' + str(count) 
		os.mkdir(zipPath)
		for file in file_list:
			filePath = os.path.join(path, file)
			shutil.move(filePath, zipPath)
		shutil.make_archive(zipPath, 'zip', zipPath)
		packedFiles = os.listdir(zipPath)
		for i in packedFiles:
			iPath = os.path.join(zipPath, i)
			os.remove(iPath)
		os.rmdir(zipPath)
		file_list = []




