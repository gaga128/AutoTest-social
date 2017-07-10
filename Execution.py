# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-17
# Description:
#****************************************************************
import json
import checkPoint
import xlrd
import writeLog
import writeExcelresult
import os




##########预期结果与实际结果转换成json格式进行对比
def acex(AC_result,EX_result):
	actualresult = json.loads(AC_result)  # 改为json格式
	datas = actualresult["datas"]  # 取key对应的value
	flag = actualresult["flag"]
	desc = actualresult["desc"]
	expectresult = json.loads(EX_result)
	Edatas = expectresult["datas"]
	Edesc = expectresult["desc"]
	Eflag = expectresult["flag"]
	finalresult = checkPoint.check_result(datas, Edatas, desc, Edesc, flag, Eflag,'n')
	return finalresult



############对比结果或者写入结果--参数配置############
def Executionmode(runresult,casepath,casesheet,resultname):
	bk = xlrd.open_workbook(casepath, formatting_info=True)  # 打开excel文件
	if resultname in bk.sheet_names():
		ch = bk.sheet_by_name(resultname)
		nrows = ch.nrows
		ncols = ch.ncols
		# print runresult
		resultlist=runresult[1::2]
		for m in range(1, nrows):
			AC_result = resultlist[m - 1]
			# print AC_result
			EX_result = ch.cell_value(m, ncols - 1)
			eachcase = ch.cell_value(m, ncols - 2)
			finalresult = acex(AC_result, EX_result)
			if finalresult == False:
				writeLog.errorlog('FAIL:wrong datas case is number:case%s' % m, eachcase)
	else:
		# print runresult
		writeExcelresult.writeResult(runresult,casepath,casesheet,resultname)




##############不同参数类型的写入结果或结果对比###################
def Executionmode2(runresult,casepath,resultname):
	bk = xlrd.open_workbook(casepath, formatting_info=True)  # 打开excel文件
	resultlist = runresult[1::2]
	caselist=runresult[0::2]
	if resultname in bk.sheet_names():
		ch = bk.sheet_by_name(resultname)
		nrows = ch.nrows
		ncols = ch.ncols
		# print runresult
		for m in range(1, nrows):
			AC_result = resultlist[m - 1]
			# print AC_result
			EX_result = ch.cell_value(m, ncols - 1)
			eachcase = ch.cell_value(m, ncols - 2)
			finalresult = acex(AC_result, EX_result)
			if finalresult == False:
				writeLog.errorlog('FAIL:wrong datas case is number:case%s' % m, eachcase)
	else:
		# print runresult
		checkpass=[]
		for i in range(0,len(runresult[1::2])):
			result=json.loads(resultlist[i])
			data = result["datas"]  # 取key对应的value
			flag = result["flag"]
			desc = result["desc"]
		 	if desc=="参数错误" and flag==3:
				teststate='pass'
			else:
				teststate='Need verify'
			checkpass.append(teststate)
		# print checkpass
		results=[]

		for i in zip(checkpass,caselist,resultlist):
			results.extend(list(i))
		# print results
		writeExcelresult.writeResult2(results,casepath,resultname)



##############空&特殊字符写入结果或结果对比###################
def Executionmode1(runresult, casepath, resultname):
	bk = xlrd.open_workbook(casepath, formatting_info=True)  # 打开excel文件
	if resultname in bk.sheet_names():
		ch = bk.sheet_by_name(resultname)
		nrows = ch.nrows
		ncols = ch.ncols
		# print runresult
		resultlist = runresult[1::2]
		for m in range(1, nrows):
			AC_result = resultlist[m - 1]
			# print AC_result
			EX_result = ch.cell_value(m, ncols - 1)
			eachcase = ch.cell_value(m, ncols - 2)
			finalresult = acex(AC_result, EX_result)
			if finalresult == False:
				writeLog.errorlog('FAIL:wrong datas case is number:case%s' % m, eachcase)
	else:
		# print runresult
		writeExcelresult.writeResult1(runresult, casepath, resultname)

















#########################################################################
if __name__ == '__main__' :
	acex('{"datas":"","desc":"参数错误","flag":3,"usetime":1}','{"datas":"执行失败","desc":"执行成功","flag":200,"usetime":2}')
	Executionmode2([u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&appkey=15.5', u'{"datas":{"detail":[],"totalRecordSize":0},"desc":"\u6267\u884c\u6210\u529f","flag":200,"usetime":3}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&appkey=string', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&appkey=False', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&tagId=15.5', u'{"datas":{"detail":[],"totalRecordSize":0},"desc":"\u6267\u884c\u6210\u529f","flag":200,"usetime":4}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&tagId=string', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":0}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&tagId=False', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&page=15.5', u'{"datas":{"detail":[],"totalRecordSize":0},"desc":"\u6267\u884c\u6210\u529f","flag":200,"usetime":4}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&page=string', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":0}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&page=False', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":0}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&pageSize=15.5', u'{"datas":{"detail":[],"totalRecordSize":0},"desc":"\u6267\u884c\u6210\u529f","flag":200,"usetime":4}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&pageSize=string', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&propertyName=life_cycle&propertyValue=Mature+Consumer&sortFlag=True&sortPropertyName=interact&sortType=asc&pageSize=False', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortPropertyName=interact&sortType=asc&sortFlag=1', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":1}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortPropertyName=interact&sortType=asc&sortFlag=15.5', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":0}', u'http://211.151.58.219:10091/cdapi/req?appid=444&passwd=746749378&method=getFansListByFanPropertyAndTagCondi&appkey=172140270&tagId=913&classId=718&page=1&pageSize=100&propertyName=life_cycle&propertyValue=Mature+Consumer&sortPropertyName=interact&sortType=asc&sortFlag=string', u'{"datas":"","desc":"\u53c2\u6570\u9519\u8bef","flag":3,"usetime":0}'],os.getcwd() + r'/mycase/demo.xls', 'AutotypeCaRe')