import os 
import shutil
import threading

"""
自动扫描压缩包并解压，然后删除压缩包

"""

class ZipManager:

		def __init__(self, file_path):
			self.file_path = file_path 

		def scanf(self):
			files = os.listdir(self.file_path)
			for f in files:
				if f.endswith('zip'):
					return f

		def un_zip(self, f):
			if f:
				path = f.split('.')[0]
				filePath = self.file_path + '/' + f   
				target_path = self.file_path + '/' + path
				# os.mkdir(target_path)
				shutil.unpack_archive(filePath, target_path)

		def delete(self, f):
			if f:
				filePath = self.file_path + '/' + f   
				os.remove(filePath)

		def move(self, f):
			if not os.path.exists('/home/bo/Downloads/packages'):
				os.mkdir('/home/bo/Downloads/packages')
			if f:
				file = '/home/bo/Downloads/' + f
				shutil.move(file, '/home/bo/Downloads/packages')


		def run(self):
			if self.file_path == '/home/bo/Desktop':
				f = self.scanf()
				self.un_zip(f)
				self.delete(f)
			if self.file_path == '/home/bo/Downloads':
				f = self.scanf()
				self.un_zip(f)
				self.move(f)





manager1 = ZipManager('/home/bo/Desktop')
manager2 = ZipManager('/home/bo/Downloads')
print(manager1)
print(manager2)
print('正在监测压缩文件...')
while True:
	manager1.run()
	manager2.run()