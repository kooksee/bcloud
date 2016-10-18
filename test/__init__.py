#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText

# 要发给谁
mail_to = "kooksee@163.com"


def send_mail(to_list, sub, content):
    # 设置服务器，用户名、口令以及邮箱的后缀
    mail_host = "smtp.163.com"
    mail_user = "****"
    mail_pass = "****"
    mail_postfix = "163.com"
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        print '1'
        return True
    except Exception, e:
        print '2'
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mail_to, "hello", "this is python sent"):
        print "发送成功"
    else:
        print "发送失败"
