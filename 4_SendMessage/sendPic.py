from wxpy import *

bot = Bot()
name_list = ['胡松江', '付春龍', '青影']
text = 'Hi~{}!'
for name in name_list:
	friend = bot.friends().search(name)[0]
	message = text.format(name)
	friend.send(message)

