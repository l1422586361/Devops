# -*- coding:utf-8 -*-
# @Time : 2020/4/25 16:18
# @Author: lin
# @File : demo.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(to_mail,to_subject,to_msg):


    # 设置smtplib所需的参数
    # 下面的发件人，收件人是用于邮件传输的。
    smtpserver = 'smtp.qq.com'
    username = '1422586361@qq.com'
    password = 'xbuixxxxbagi' # 授权码，上传网上需修改
    sender = '1422586361@qq.com'
    receiver = 'linweitao@kingyea.com.cn' #收件人
    # receiver = ['XXX@126.com', 'XXX@126.com'] 多人收件

    # 邮件对象
    msg = MIMEMultipart('mixed')
    msg['Subject'] = to_subject
    msg['From'] = sender    # 代表xx人发件，默认写的自己，可以改成其他人的邮箱
    msg['To'] = receiver
    # msg['To'] = ";".join(receiver) 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串

    # 构造文字内容
    text_plain = MIMEText(to_msg,'plain','utf-8')
    msg.attach(text_plain)


    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        # 使用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
        # smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print('>>>>>>>:'+ e)

if __name__ == '__main__':
    with open('/sys/class/power_supply/Battery/capacity','r') as f:
        line = int(f.read())
        if line <= 50:
            to_mail = 'linweitao@kingyea.com.cn'
            send_subject = '充电通知'
            send_msg = "Your server's current capacity is: <%s> ,Please charge in time!!" % line
            sendMail(to_mail,send_subject,send_msg)
