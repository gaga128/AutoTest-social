# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-06
# Description:
#****************************************************************
import xlrd
import itertools
import os
import Requesttype
import getvalue
import writeExcelresult
import Execution
import writeLog
import FileOperation
"""
casepath：传入用例路径
处理excel用例
取得并拼接参数列表
调用封装的http请求
执行用例
"""

permission1 = ['appid=444','passwd=746749378']
permission2 = ['"appid":"444"','"passwd":"746749378"']

def createcase(casepath,defaultname,resultname,Speparamlist):
	bk = xlrd.open_workbook(casepath,formatting_info=True)  # 打开excel文件
	httpString = bk.sheet_by_name('Sheet1').cell_value(0, 0)  # 接口url在表1里
	sh = bk.sheet_by_name(defaultname)
	runFirstnullresult = []
	methods = sh.cell_value(1, 1)
	a = FileOperation.FileExsit(os.getcwd() + r'/log/failresult.html')
	if a == True:
		FileOperation.DelFile(os.getcwd() + r'/log/failresult.html')
	try:

		list1 = getvalue.getdvalue(casepath, defaultname, methods)
		if methods == 'GET':
			mypermission = permission1
		else:
			mypermission = permission2
		for i in range(len(list1) - 1, len(list1)):  ###大于等于列表长度-1参数
			nulllist = []
			iter = itertools.combinations(list1, i)  ###i表示取列表中的n个参数进行组合
			nulllist.append(list(iter))  ######iter是一个循环器，所以它的值只能用1次，需要把值存到变量里
		# print nulllist
		for j in range(0, len(nulllist[0])):  ####生成列表个数
			parameter1 = mypermission
			parameter2 = list(nulllist[0][j])
			testcase = parameter1 + parameter2
			# print testcase
			AC_result = Requesttype.Requesttype(methods, testcase, httpString)
			eachcase = Requesttype.Requestcase(methods, testcase, httpString)
			# print eachcase
			# print EX_result
			runFirstnullresult.append(eachcase)
			runFirstnullresult.append(AC_result)
		for i in range(0, len(list1)):
			for y in Speparamlist:
				parameter1 = getvalue.getdvalue(casepath, defaultname, methods)
				x = sh.cell_value(i + 4, 0)
				if methods == 'GET':
					element2 = x + '=' + y
				else:
					element2 = '"' + x + '":"' + y + '"'
				parameter1.pop(i)
				# print list1
				parameter1.append(element2)
				# print parameter1
				parameter = mypermission
				testcase = parameter + parameter1
				AC_result = Requesttype.Requesttype(methods, testcase, httpString)
				print AC_result
				eachcase = Requesttype.Requestcase(methods, testcase, httpString)
				runFirstnullresult.append(eachcase)
				runFirstnullresult.append(AC_result)
		# print runFirstnullresult
		return runFirstnullresult
		Execution.Executionmode1(runFirstnullresult, casepath, resultname)

	except Exception, e:
		print e
#########################################################################
if __name__ == '__main__' :
	runFirstnullresult=createcase(os.getcwd()+r'/mycase/demo.xls','Default parameter','AutoCaRe',['','&'])
	Execution.Executionmode1(runFirstnullresult, os.getcwd() + r'/mycase/demo.xls', 'AutoCaRe')