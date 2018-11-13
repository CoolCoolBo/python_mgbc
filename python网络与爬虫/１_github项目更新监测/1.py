import requests
import webbrowser
import time





starred_list = []
starred_info = requests.get('https://api.github.com/users/CoolCoolBo/starred').json()
for e in starred_info:
    starred_list.append(e['id'])
while True:
    print('正在监测...')
    cur_starred = requests.get('https://api.github.com/users/CoolCoolBo/starred').json()
    for each in cur_starred:
        if each['id'] not in starred_list:
            starred_list.append(each['id']) 
            owner = each['owner']['login']
            repo_name = each['full_name']
            url = "https://github.com/" + repo_name
            print(url)
            webbrowser.open(url)
    time.sleep(10)
            # owner = each['owner']['login']
            # repo_name = each['full_name']
            # url = "https://github.com/" + owner + '/' + repo_name
            # print(url)
            # webbrowser.open(url)
