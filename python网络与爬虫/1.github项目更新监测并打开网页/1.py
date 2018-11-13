import requests
import webbrowser
import time


def get_curList(api_url):
    starred_info = requests.get(api_url).json()
    print(starred_info)
    for each in starred_info:
        cur_list.append(each['id'])
    return cur_list


def open_newRepo(cur_list, last_list):
    for cur in cur_list:
        if cur not in last_list:
            owner = cur['owner']['login']
            repo_name = cur['full_name']
            url = "https://github.com/" + owner + '/' + repo_name
            print(url)
            # webbrowser.open('www.baidu.com')

last_list = None
cur_list = []
while True:
    cur_list = get_curList('https://api.github.com/users/kennethreitz/starred')
    print('正在监测中')
    print('The cur_list is: ', cur_list)
    if not last_list:
        last_list = cur_list
    # open_newRepo(cur_list, last_list)
    last_list = cur_list
    print('The last_list is: ', last_list)
    time.sleep(10)
