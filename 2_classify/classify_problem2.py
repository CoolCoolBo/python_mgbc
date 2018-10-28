import os
import shutil

"""
将problem2_files里面各个文件里面的东西整理并分为image和document两类

"""

image_folder_list = ['jpg', 'png', 'gif']
document_folder_list = ['doc', 'docx', 'md', 'ppt']
path = './problem2_files'
folders = os.listdir(path)
image_folder_path = './problem2_files/images' 
document_folder_path = './problem2_files/documents' 
image = os.mkdir(image_folder_path)
document = os.mkdir(document_folder_path)

def classify(folder, folder_path):
	folder = os.path.join(path, folder)
	files = os.listdir(folder)
	for file in files:
		file = os.path.join(folder, file)
		shutil.move(file, folder_path)
		
for folder in folders:

	if folder in image_folder_list:
		classify(folder, image_folder_path)

	if folder in document_folder_list:
		classify(folder, document_folder_path)

