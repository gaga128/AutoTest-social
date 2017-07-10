# -*- coding: utf-8 -*-
#****************************************************************
# myEmail.py
# Author     : hsn
# Version    : 1.0
# Date       : 2016-05-11
# Description:
#****************************************************************
import smtplib,os
import myEmail
import FileOperation

def sendEmail():
    """
    发送邮件
    """
    failcase = os.path.dirname(os.path.abspath(__file__)) + r'\log\failresult.html'
    Failtest = []
    isFExists =  FileOperation.FileExsit(failcase)
    # print isFExists
    if not isFExists:
        pass
    else:
        Failtest = ['%s'%(failcase)]
    MSG_TEXT = "failed case result addreass : 到时候我会把附件里的文件放到服务器上，然后这个位置放个链接。目前暂时打开附件查看。"
    myEmail.SendEmailWithAttachment('huangshengnan@social-touch.com',['huangshengnan@social-touch.com','lujia@social-touch.com'],'AutoTestResult-sentbyHSN',MSG_TEXT,Failtest,'smtp.qiye.163.com:25')
    print u"邮件已发送"


if __name__ == '__main__':
    sendEmail()
