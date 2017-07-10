# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-19
# Description:
#****************************************************************
import xlrd
import os
import writeExcelresult
import Execution
import writeLog
import Requesttype
import FileOperation
import uuid
"""
casepath：传入用例路径
处理excel用例
取得并拼接参数列表
调用封装的http请求
执行用例
"""
def runcase(casepath,sheetname,resultname):
	bk = xlrd.open_workbook(casepath)  # 打开excel文件
	httpString = bk.sheet_by_name('Sheet1').cell_value(0, 0)  # 接口url在表1里
	sh = bk.sheet_by_name(sheetname)  # 测试数据在表2里
	mrows = sh.nrows
	mcols = sh.ncols
	runFirstresult=[]

	a = FileOperation.FileExsit(os.getcwd() +r'/log/failresult.html')
	if a == True:
		FileOperation.DelFile(os.getcwd() +r'/log/failresult.html')

	try:      #拼接参数名与参数值
		for j in range(1,mrows):
			methods = sh.cell_value(j, 2)
			testcase=[]
			for i in range(3,mcols):
				x = sh.cell_value(0,i )  # 参数名,获取单元格的数据类型
				y = sh.cell_value(j,i)  # 参数值
				xtype = sh.cell(0, i).ctype
				ytype = sh.cell(j,i).ctype
				###################ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
				if (xtype == 2):
					x = str(int(x))
				if (ytype == 2) or (ytype == 4):
					y = str(int(y))
					y = str(y)
				if x.find(' ') != -1 or y.find(' ') != -1:
					x = x.replace(' ', '+')
					y = y.replace(' ', '+')
				if ytype == 4 and y == '1':
					y = 'True'
				elif ytype == 4 and y == '0':
					y = 'False'
				if methods == 'GET':
					element2 = x + '=' + y
				else:
					element2 = '"' + x + '":"' + y + '"'
				testcase.append(element2)
			# print testcase
			AC_result = Requesttype.Requesttype(methods, testcase, httpString)
			eachcase = Requesttype.Requestcase(methods, testcase, httpString)
			print AC_result
			runFirstresult.append(eachcase)
			runFirstresult.append(AC_result)
		# print runFirstresult
		return runFirstresult
		Execution.Executionmode(runFirstresult, casepath, casesheet,resultname)





	except Exception, e:
		print e


#########################################################################
if __name__ == '__main__':
	runFirstresult = runcase(os.getcwd() + r'/mycase/demo.xls','Sheet2','CaRe')
	Execution.Executionmode(runFirstresult, os.getcwd() + r'/mycase/demo.xls', 'Sheet2' ,'CaRe')