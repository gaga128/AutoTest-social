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


def createtypecase(casepath,defaultname,resultname,Speparamlist):
	bk = xlrd.open_workbook(casepath,formatting_info=True)  # 打开excel文件
	httpString = bk.sheet_by_name('Sheet1').cell_value(0, 0)  # 接口url在表1里
	sh = bk.sheet_by_name(defaultname)
	nrows=sh.nrows
	runresult=[]
	methods = sh.cell_value(1, 1)

	a = FileOperation.FileExsit(os.getcwd() + r'/log/failresult.html')
	if a == True:
		FileOperation.DelFile(os.getcwd() + r'/log/failresult.html')


	try:

		list1 = getvalue.getdvalue(casepath, defaultname, methods)
		# print list1
		if methods == 'GET':
			mypermission = permission1
		else:
			mypermission = permission2
		for i in range(5, nrows):  ##所在行
			x = sh.cell_value(i, 0)  # 参数名,获取单元格的数据类型
			y = sh.cell_value(i, 1)  # 参数值
			z = sh.cell_value(i, 2)  #参数类型
			if z=='str':
				pass
				# print '不替换字符串类型参数'
			else:
				z="<type '%s'>"%z
				testlist = []
				for j in range(0,len(Speparamlist)):
					deparamtype=type(Speparamlist[j])
					if z==str(deparamtype):
						pass
						# print '取出同类型参数不进行替换'
					else:
						testlist.append(Speparamlist[j])
				# print testlist
				for n in range(0,len(testlist)):
					y=str(testlist[n])
					x = sh.cell_value(i, 0)
					# print x
					parameter1 = getvalue.getdvalue(casepath, defaultname, methods)
					# print parameter1
					if methods == 'GET':
						element2 = x + '=' + y
					else:
						element2 = '"' + x + '":"' + y + '"'
					# print element2
					parameter1.pop(i-4)
					parameter1.append(element2)
					# print parameter1
					parameter = mypermission
					testcase = parameter + parameter1
					# print testcase
					AC_result = Requesttype.Requesttype(methods, testcase, httpString)
					print AC_result
					eachcase = Requesttype.Requestcase(methods, testcase, httpString)
					runresult.append(eachcase)
					runresult.append(AC_result)
		# print runresult
		return runresult

		Execution.Executionmode(runresult, casepath,resultname,)

	except Exception, e:
		print e



if __name__ == '__main__' :
	runresult=createtypecase(os.getcwd()+r'/mycase/demo.xls','Default parameter','AutotypeCaRe',[1,15.5,'string',False])
	Execution.Executionmode2(runresult, os.getcwd() + r'/mycase/demo.xls','AutotypeCaRe')
