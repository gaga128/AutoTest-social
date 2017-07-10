# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-17
# Description:
#****************************************************************
import xlrd
import os
import httpRequests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
casepath：传入用例路径
处理excel用例
取得并拼接参数列表
调用封装的http请求
执行用例
"""
permission = ['appid=444','passwd=746749378']

def getdvalue(casepath,sheetname,methods):
	bk = xlrd.open_workbook(casepath,formatting_info=True)  # 打开excel文件
	httpString = bk.sheet_by_name('Sheet1').cell_value(0, 0)  # 接口url在表1里
	sh = bk.sheet_by_name(sheetname)
	nrows = sh.nrows
	mylist=[]
	myvalue=[]

	try:     #拼接参数名与参数值
		for i in range(4, nrows):  ##所在行
			x = sh.cell_value(i, 0)  # 参数名,获取单元格的数据类型
			y = sh.cell_value(i, 1)  # 参数值
			xtype = sh.cell(i, 0).ctype
			ytype = sh.cell(i, 1).ctype
			###################ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
			if (xtype == 2):
				x = str(int(x))
			if (ytype == 2) or (ytype == 4):
				y = str(int(y))
			if x.find(' ') != -1 or y.find(' ') != -1:
				x = x.replace(' ', '+')
				y = y.replace(' ', '+')
			if ytype == 4 and y == '1':
				y = 'True'
			elif ytype == 4 and y == '0':
				y = 'False'
			param = x + '=' + y  # 不加双引号
			# print param
			value = '"' + x + '":"' + y + '"'
			mylist.append(param)  ###向列表内增加参数
			myvalue.append(value)
		# print myvalue
		# print mylist
		fulllist = permission + mylist
		Fullparams = '&'.join(fulllist)
		# print Fullparams
		Resultcheck = httpRequests.httpRequests(httpString, Fullparams, 'GET')
		# print Resultcheck
		Resultcheck = json.loads(Resultcheck)

		if Resultcheck['flag'] != 200:
			print "请求结果错误，请确认参数配置是否正确！"
		else:
			if methods == 'GET':
				list1=mylist
			else:
				list1=myvalue
		# print list1
		return list1

	except Exception, e:
		print e


#########################################################################
if __name__ == '__main__' :
	getdvalue(os.getcwd()+r'/mycase/demo.xls','Default parameter',"GET")