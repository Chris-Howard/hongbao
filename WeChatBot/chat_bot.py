#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

from requests_html import HTMLSession
from wxpy import *
import time

session = HTMLSession()
server = 'https://hongbao.xxooweb.com/hongbao'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 初次使用需要输入手机号码，保存在phone.txt中
try:
    with open('phone.txt','r') as phone:
        mobile=phone.read()
except:
    mobile = input('请输入手机号码：')
    with open('phone.txt', 'w') as phone:
        phone.write(mobile)

count = 0
bot = Bot()

# 别太贪心，一天三个红包还嫌不够吗
while count<=3:

    # 定时任务：每过3秒读取一次新的消息并尝试抢红包
    time.sleep(3)

    for i,sharing in enumerate(bot.messages.search('饿了么')+bot.messages.search('美团')):
        r = session.post(server, {'url': sharing.url, 'mobile': mobile, 'headers': header})
        if r.text:
            print('已抢了{}次红包~'.format(count+1))
            msg = json.loads(r.text)
            try:
                print(msg['message'])
            except:
                pass
            print('\n-----------------\n')
            if '领取完毕' in msg['message']:
                count+=1
        if bot.messages:
            bot.messages.pop(i)