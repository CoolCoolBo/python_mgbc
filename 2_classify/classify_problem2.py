import os
import shutil

image_folder_list = ['jpg', 'png', 'gif']
document_folder_list = ['doc', 'docx', 'md', 'ppt']
path = './problem2_files'
folders = os.listdir(path)
image_folder_path = './problem2_files/images' 
document_folder_path = './problem2_files/documents' 
image = os.mkdir(image_folder_path)
document = os.mkdir(document_folder_path)

for folder in folders:

	if folder in image_folder_list:
		folder = os.path.join(path, folder)
		files = os.listdir(folder)
		for file in files:
			file = os.path.join(folder, file)
			shutil.move(file, image_folder_path)

	if folder in document_folder_list:
		folder = os.path.join(path, folder)
		files = os.listdir(folder)
		for file in files:
			file = os.path.join(folder, file)
			shutil.move(file, document_folder_path)

