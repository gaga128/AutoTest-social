# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-20
# Description:
#****************************************************************

import os

allfileNum=0

def readfile(path):
	global allfileNum    #####将变量定义为全局变量
	filelist=[]
	files=os.listdir(path)   ####listdir获取指定目录中的内容存入列表中
	for f in files:
		if (os.path.isfile(path + f)):
			if f[0]=='.':
				pass
			else:
				filelist.append(f)
				allfileNum = allfileNum + 1
	print filelist
	return filelist

########################################################################
if __name__ == '__main__' :
	readfile(os.getcwd()+r'/mycase/')
	print '总文件数 =', allfileNum
