# -*- coding: utf-8 -*-
#****************************************************************
# myEmail.py
# Author     : hsn
# Version    : 1.0
# Date       : 2016-05-11
# Description:
#****************************************************************
import smtplib,os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def SendEmailWithAttachment(send_from, send_to, subject, text, files=[], server="localhost"):
    """
    邮件初始化定义
    定义发件服务器用户名密码
    编辑附件
    send_from：发件人
    send_to：收件人列表
    subject：邮件主题
    text：正文文本
    files：附件列表
    server：服务器默认本地
    """
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(f,"rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    username = 'bdtest@social-touch.com'
    password = 'fzd337x4'
    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


#################################################################
if __name__ == '__main__':
    Emailpath = os.path.dirname(os.path.abspath(__file__)) + r'\log\failresult.html'
    #failcase=['%s'%(Emailpath)]
    SendEmailWithAttachment('huangshengnan@social-touch.com',['huangshengnan@social-touch.com'],'test','test email','failcase','smtp.qiye.163.com:25')