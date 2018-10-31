from wxpy import *
import csv

def sendMessage(info_list, text):
	bot = Bot()
	for each in info_list:
		message = text.format(name=each['微信昵称'], 
							   time=each['时间'], 
							   event=each['事件'],
							   place=each['地址'],
							   note=each['备注'])
		friend = bot.friends().search(each['微信昵称']) 
		if len(friend) == 1:
			try:
				friend[0].send(message)
			except ResponseError as e:
				print(e.err_code, e.err_msg)
		else:
			print("找不到该用户：　"，each['微信昵称'])
		time.sleep(1)

file = open('./MeetingMsg.csv', 'r')
csv_file = csv.DictReader(file)
text = '{name},提醒下，{time}记得来参加{event},地点在{place},{note}'
info_list = [info for info in csv_file]
sendMessage(info_list, text)
file.close()
