#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-06
# Description:
#****************************************************************
import xlrd
import xlutils
from xlutils.copy import copy
import os


######################写入请求结果########################################
def writeResult(runresult,resultpath,casesheet,caseresult):
	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
	if caseresult in oldE.sheet_names():                    ####给出sheetname列表
		print 'Expected results exist!'
	else:
		newE=copy(oldE)
		nwr=newE.add_sheet(caseresult, cell_overwrite_ok=True)  ##新增一个sheet1，第二参数用于确认同一个cell单元是否可以重设值。
		sh = oldE.sheet_by_name(casesheet)
		nrows = sh.nrows
		i=1
		j=1
		for line1 in runresult[1::2]:
			nwr.write(i, 3, line1)

			i = i + 1

		for line2 in runresult[0::2]:
			nwr.write(j, 2, line2)
			# nwr.write(j, 1, 'TestCase%s' % j)
			nwr.write(j, 0, '%s' % j)
			j = j + 1
		for k in range(0, nrows):
			z = sh.cell_value(k, 1)
			print z
			nwr.write(k, 1, z)

		nwr.write(0, 3, 'Expectresult')
		nwr.write(0, 2, 'URL')
		# nwr.write(0, 1, 'TestcaseName')
		nwr.write(0, 0, 'ID')
		print 'EX_result save successfully!'

		newE.save(resultpath)



#####################写入自动请求结果########################################
def writeResult1(runresult, resultpath,  caseresult):
	oldE = xlrd.open_workbook(resultpath, formatting_info=True)  ###保存之前数据的格式
	if caseresult in oldE.sheet_names():  ####给出sheetname列表
		print 'Expected results exist!'
	else:
		newE = copy(oldE)
		nwr = newE.add_sheet(caseresult, cell_overwrite_ok=True)  ##新增一个sheet1，第二参数用于确认同一个cell单元是否可以重设值。
		i = 1
		j = 1
		for line1 in runresult[1::2]:
			nwr.write(i, 3, line1)

			i = i + 1

		for line2 in runresult[0::2]:
			nwr.write(j, 2, line2)
			nwr.write(j, 1, 'TestCase%s' % j)
			nwr.write(j, 0, '%s' % j)
			j = j + 1

		nwr.write(0, 3, 'Expectresult')
		nwr.write(0, 2, 'URL')
		nwr.write(0, 1, 'TestcaseName')
		nwr.write(0, 0, 'ID')
		print 'EX_result save successfully!'

		newE.save(resultpath)














######################写入自动请求and自动验证结果########################################
def writeResult2(runresult,resultpath,sheetname):
	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
	if sheetname in oldE.sheet_names():                    ####给出sheetname列表
		print 'Expected results exist!'
	else:
		newE=copy(oldE)
		nwr=newE.add_sheet(sheetname, cell_overwrite_ok=True)  ##新增一个sheet1，第二参数用于确认同一个cell单元是否可以重设值。
		i=1
		j=1
		k=1
		for line3 in runresult[::3]:
			nwr.write(k, 2, line3)
			k = k + 1
		for line1 in runresult[1::3]:
			nwr.write(i, 3, line1)
			nwr.write(i, 1, 'TestCase%s' % i)
			nwr.write(i, 0, '%s' % i)
			i = i + 1

		for line2 in runresult[2::3]:
			nwr.write(j, 4, line2)
			j = j + 1

		nwr.write(0, 4, 'Expectresult')
		nwr.write(0, 3, 'URL')
		nwr.write(0, 2, 'checkpass')
		nwr.write(0, 1, 'TestcaseName')
		nwr.write(0, 0, 'ID')
		print 'EX_result save successfully!'
		newE.save(resultpath)


#
# ####################################在特定列后写入内容################################
# def writecase(resultpath,casesheet,caseresult):
# 	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
# 	newE=copy(oldE)
# 	nwr=newE.get_sheet(caseresult)
# 	sh = oldE.sheet_by_name(casesheet)
# 	nrows = sh.nrows
# 	for i in range(0,nrows-1):



# ####################################在测试用例最后一行写入结果################################
# def writexistseResult(runFirstresult,resultpath,sheetname):
# 	oldE=xlrd.open_workbook(resultpath,formatting_info=True)   ###保存之前数据的格式
# 	newE=copy(oldE,)
# 	nwr=newE.get_sheet(1)
# 	sh = oldE.sheet_by_name(sheetname)
# 	ncols = sh.ncols
# 	if runFirstresult==[]:
# 		return None
# 	else:
# 		i=1
#     	for line in runFirstresult:
# 			nwr.write(i,ncols,line)
#         		i = i + 1
#     	nwr.write(0,ncols,'Expectresult')
#     	newE.save(resultpath)
