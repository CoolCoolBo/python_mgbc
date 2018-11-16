# coding:utf-8
import requests


get_code_api = "https://api.github.com/search/code?q="
get_repo_api = "https://api.github.com/search/repositories?q=language:python"
# 编写函数，实现在github某一目录下寻找code文件的功能
def get_code(language, size, repo):
	print("get_code")
	url = get_code_api + "language:" + language + "+size:" + size + "+repo:" + repo

	# 访问Github接口
	info = requests.get(url).json()
	if 'items' in info:
		for i in info['items']:
			print(i['html_url'])

# 编写函数，查找更新时间在last_week之后的项目
def get_project(last_week):
	# 访问Github接口
	print("get_project")
	info = requests.get(get_repo_api).json()
	for i in info['items']:
		created_time = i['created_at']
		print(created_time)
		if created_time > last_week:
			language = 'python'
			size = "<200"

			# 从info数据中获取项目的目录
			repo = i['html_url'].replace("https://github.com/", "")
			# 传入三个限制条件，调用查找code文件的函数
			get_code(language, size, repo)

get_project("2010-11-3T00:00:00Z")