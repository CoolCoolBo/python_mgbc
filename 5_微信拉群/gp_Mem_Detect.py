from wxpy import *
import time

def isIn(members_before, members_now):
	for each in members_now:
		if each not in members_before:
			change_members.append(each.name)
			return change_members

def isOut(members_before, members_now):
	for each in members_before:
		if each not in members_now:
			change_members.append(each.name)
			return change_members

def sendOutMsg(change_members, bot):
	for member in change_members:
		msg = '{}退出了群聊'.format(member)
		print(msg)
		myself = bot.friends().search('胡松江')[0]
		myself.send(msg)

def sendInMsg(change_members, bot):
	for member in change_members:
		msg = '{}加入了群聊'.format(member)
		print(msg)
		myself = bot.friends().search('胡松江')[0]
		myself.send(msg)

bot = Bot()
group = bot.groups().search("测试群")[0]
members_before = group.members
while True:
	change_members = []
	time.sleep(10)
	group = bot.groups().search("测试群")[0]
	members_now = group.members
	if len(members_now) < len(members_before):
		change_members = isOut(members_before, members_now)
		sendOutMsg(change_members, bot)
		members_before = members_now
	elif len(members_now) > len(members_before):
		change_members = isIn(members_before, members_now)
		sendInMsg(change_members, bot)
		members_before = members_now

