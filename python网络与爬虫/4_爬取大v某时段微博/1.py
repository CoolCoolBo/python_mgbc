from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import csv


def start_chrome():
	driver = webdriver.Chrome(executable_path='./chromedriver')
	driver.start_client()
	return driver

def query(s_time, e_time):
	return f'?is_ori=1&key_word=&start_time={s_time}&end_time={e_time}&is_search=1&is_searchadv=1#_0'

def scroll_down():
	html_page = driver.find_element_by_tag_name('html')
	for i in range(5):
		print(i)
		html_page.send_keys(Keys.END)
		time.sleep(0.6)

def find_info():
	cards_sel = 'div.WB_feed_detail'
	cards = driver.find_elements_by_css_selector(cards_sel)
	info_list = []
	for card in cards:
		print(card)
		content_sel = 'div.WB_text.W_f14'
		time_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'
		link_sel = 'div.WB_from.S_txt2 > a:nth-child(1)'

		content = card.find_element_by_css_selector(content_sel).text
		time = card.find_elements_by_css_selector(time_sel)[0].get_attribute('title')
		link = card.find_elements_by_css_selector(link_sel)[0].get_attribute('href')

		info_list.append([content, time, link])
	return info_list

def find_next():
	next_sel = 'a.page.next'
	next_page = driver.find_elements_by_css_selector(next_sel)
	if next_page:
		return next_page[0].get_attribute('href')

def save(info_list, name):
	full_path = './' + name + '.csv'
	if os.path.exists(full_path):
		with open(full_path, 'a') as f:
			writer = csv.writer(f)
			writer.writerows(info_list)
			print('Done')
	else:
		with open(full_path, 'w+') as f:
			writer = csv.writer(f)
			writer.writerows(info_list)
			print('Done')

def run_crawler(base, duration):
	# 如果网页不是以feedtop结尾，访问查询页
	if not base.endswith('feedtop'):
		st, et = duration.split('~')
		driver.get(base + query(st, et))
	# 如果网页以feedtop结尾，说明得到的是下一页的地址,直接访问
	else:
		driver.get(base)
	time.sleep(5)
	scroll_down()
	time.sleep(5)
	info_list = find_info()
	save(info_list, duration)
	next_page = find_next()
	if next_page:
		run_crawler(next_page, duration)


base = 'https://weibo.com/bgsxy'
driver = start_chrome()
driver.get(base)
time.sleep(30)
run_crawler(base, '2018-08-01~2018-12-03')
