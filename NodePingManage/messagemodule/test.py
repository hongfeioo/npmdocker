#!/usr/bin/python
#coding=utf-8
import time

import messageMode


muti_phone = '13521161889'
muti_mail = 'yihf@liepin.com'
arg_msg = 'baby,Be careful on the road'
begintime =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

messageMode.send_muti_sms(muti_phone,0,'hello baby',arg_msg)
messageMode.sendtxtmail('becare baby',0,arg_msg,muti_mail,begintime)


print 'ok'
