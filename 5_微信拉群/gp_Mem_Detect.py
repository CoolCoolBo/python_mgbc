# coding=utf-8
from wxpy import *
import time


def isIn(change_members, members_before, members_now):
    for each in members_now:
        if each not in members_before:
            change_members.append(each.name)
            return change_members


def isOut(change_members, members_before, members_now):
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


def listen(group_name):
    bot = Bot()
    group = bot.groups().search(group_name)[0]
    members_before = group.members
    while True:
        change_members = []
        time.sleep(30)
        group = bot.groups().search(group_name)[0]
        members_now = group.members
        if len(members_now) < len(members_before):
            change_members = isOut(change_members, members_before, members_now)
            sendOutMsg(change_members, bot)
            members_before = members_now
        elif len(members_now) > len(members_before):
            change_members = isIn(change_members, members_before, members_now)
            sendInMsg(change_members, bot)
            members_before = members_now


group_name = input("输入要监测的群：")
listen(group_name)
