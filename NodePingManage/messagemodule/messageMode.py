#!/usr/bin/python
#coding=utf-8
#filename: messageMode.py
#from collections import defaultdict
import telnetlib
import os,sys,commands,multiprocessing
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#import random
import urllib2


#---init Time---
begintime =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#---receiver config------
muti_phone='13521161889'
muti_mail='yihf@liepin.com'

#-----log file---------
pythonlog ='./sms_mail.log'


#---send mail server config--------
sender = ''
smtpserver = 'smtp.xxx.com'
username = ''
password = ''

#-----message channel-----------------
sms_string = 'http://xxx/smsweb/send4vpn.do?clientId=60004&tel='
#----------

def send_muti_sms(_fuc_muti_phone,_sms_off,_log_title,_content):
    sendtime =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    for sms_index in range(0, len(_fuc_muti_phone.split(';'))):
        if _sms_off == 1:
            break
        every_phone = _fuc_muti_phone.split(';')[sms_index]
        _content = _content.replace(chr(34),"\"")                                           #replace " to \"
        if len(_content) > 230:
            _content = _content[:230]                                                       # cut the string to 300
        sms_send_string = sms_string + every_phone+ '&context='+urllib2.quote(_content)     #according to your message channel ,may be you should change here
        print sms_send_string
        #---if find null in the phone , pass this phone num
        if every_phone.find('null') == -1:
            request =  urllib2.Request(sms_send_string)
            try:
                urllib2.urlopen(request)
                os.system("echo "+sendtime+' '+_log_title+' '+every_phone+" message send to  push.lietou.com ok >> "+pythonlog)
            except urllib2.HTTPError,e:
                os.system("echo "+sendtime+' '+_log_title+' '+every_phone+" message send HTTPError "+str(e.code)+str(e.reason)+" - -! >> "+pythonlog)
                print "http Error:",e.code,e.reason
            except urllib2.URLError,e:
                os.system("echo "+sendtime+' '+_log_title+' '+every_phone+" message send URLError "+str(e.reason)+" - -! >> "+pythonlog)
                print "URLError",e.reason
            else:
                print "send mail ok"


def sendtxtmail(_subject,_mail_off,_msg,_fuc_mail,_begintime):
    for mail_index in range(0, len(_fuc_mail.split(';'))):
        if _mail_off == 1:
            break
        _receiver =  _fuc_mail.split(';')[mail_index]
        if _receiver.find('null') == -1:
            try:
                msg = MIMEText('<html>'+_msg+'</html>','html','utf-8')
                msg['Subject'] =  _subject
                msg['to'] = _receiver
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)
                smtp.login(username, password)
                smtp.sendmail(sender,_receiver, msg.as_string())
                smtp.quit()
                os.system("echo "+_begintime+' '+_subject+' '+_receiver+" mail send successful >> "+pythonlog)
                print "mail send successful"
            except Exception,e:
                print "mail send fail"
                print e[1]
                os.system("echo "+_begintime+' '+_subject+' '+_receiver+" mail send fail ,Code: "+str(e[0])+' '+e[1].split()[0]+'- -! >>'+pythonlog)
    return 'mail func over'




def main(arg_msg):
    send_muti_sms(muti_phone,0,'test_title',arg_msg)
    sendtxtmail('test_subject',0,arg_msg,muti_mail,begintime)
    return 'main func over'

        


if __name__ == "__main__":
   print main(sys.argv[1])
