import wxpy

# members = []
# for member in group:
# 	members.append(member)
for member in members:
	result = group.search(member.name)
	if result == None:

def isIn(group):
	for each in members_now:
		if each not in members_before:
			change_members.append(each.name)
			return change_members

def isOut(group):
	for each in members_before:
		if each not in members_now:
			change_members.append(each.name)
			return change_members

def sendMsg(change_members):
	for member in change_members:
		msg = '{}已经退出群聊'.format(member.name)
		print(msg)

bot = Bot()
group = bot.groups().search("小铃铛网咖活动交流群")[0]
members_before = group.members
while True:
	# members_before = group.members
	change_members = []
	time.sleep(60)
	members_now = group.members
	if len(members_now) < len(members_before):
		change_members = isOut(group)
		sendMsg(change_members)
		members_before = members_now
	elif len(members_now) > len(members_before):
		change_members = isIn(group)
		sendMsg(change_members)
		members_before = members_now

