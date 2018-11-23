from selenium import webdriver
import time


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver
# 启动同一目录下的专用浏览器


def find_info():
    # xpath
    sel = '//*[@id="Pl_Official_MyProfileFeed__21"]/div/div[2]/div[2]/div//em[2]'
    elems = driver.find_elements_by_xpath(sel)
    return [int(el.text) for el in elems[1:]]
# 提取所需信息


while True:
    driver = start_chrome()
    # 用浏览器访问当前网址
    driver.get('https://weibo.com/bgsxy?is_hot=1')
    time.sleep(6)
    info = find_info()
    print(info)
    retweet, commit, like = info
    # 如果点赞数超过10000，则退出循环
    if like > 10000:
        break
