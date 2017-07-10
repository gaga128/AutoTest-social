# -*- coding: utf-8 -*-
#****************************************************************
# writeLog.py
# Author     : jia
# Version    : 1.0
# Date       : 2016-5-5
# Description:
#****************************************************************
import logging
import time
import FileOperation
import os


def WriteLog(error=None,info=None,debug=None):
    """
    写log
    """
    otherstyletime=time.strftime("%Y%m%d_%H.%M.%S", time.localtime(int(time.time())))
    Today=str(otherstyletime)
	#print Today
    LOG_FILENAME='./log/%s_log.txt'%Today
	#print LOG_FILENAME
    logging.basicConfig(level=logging.INFO,
						format='%(asctime)s_%(levelname)s-->%(message)s',
						datefmt='%a,%d %b %Y %H:%M:%S',
						filename=LOG_FILENAME,
						filemode='w')
    logging.error(error)
    logging.info(info)
    logging.debug(debug)

def errorlog(casenum,url):
    """
    记录错误用例
    并给出url
    """
    today = str(time.strftime("%Y-%m-%d %H.%M", time.localtime(time.time())))
    #filename = r'./log/errorlog/error_%s.htm'%today
    filename = os.path.dirname(os.path.abspath(__file__)) + r'\log\errorlog\error_%s.htm'%today
    print filename
    f=file(filename,"a+")
    f.writelines('<B>'+casenum+'</B></br>'+'<a href="'+url+'">'+url+'</a></br>')
    f.close()
    #备份失败用例，只保留最近一次
    bkup = file(os.path.dirname(os.path.abspath(__file__)) + r'\log\failresult.html','a+')#如果在Linux下备份到/opt/lampp/htdocs下可直接浏览器访问
    bkup.writelines('<B>'+casenum+'</B></br>'+'<a href="'+url+'">'+url+'</a></br>')
    bkup.close()


######################################################
if __name__ == '__main__':
##    for i in range(1,4):
##        WriteLog('test','info','debug')
    errorlog('456','http://www.baidu.com')
    WriteLog('test','info','debug')