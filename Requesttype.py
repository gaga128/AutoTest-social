# -*- coding: utf-8 -*-
#****************************************************************
# getCase.py
# Author     : Jia
# Version    : 1.0
# Date       : 2016-05-17
# Description:
#****************************************************************
import httpRequests

def Requesttype(methods,parm,httpString):
	if methods == 'GET':
		params = '&'.join(parm)
		AC_result = httpRequests.httpRequests(httpString, params, methods)
	elif methods == 'POST':
			values=','.join(parm)
			AC_result = httpRequests.httpRequests(httpString, values, methods)
	# print AC_result
	return AC_result


def Requestcase(methods,parm,httpString):
	if methods == 'GET':
		params = '&'.join(parm)
		eachcase = httpRequests.URLreturn(httpString, params)
	elif methods == 'POST':
			values=','.join(parm)
			allvalues =httpRequests.urlcode(values)
			allvalues = allvalues.replace(':', '=')
			allvalues=allvalues.replace('"','')
			eachcase =httpString+allvalues
	return eachcase


#########################################################################
if __name__ == '__main__' :
	Requesttype('GET','appid=444,passwd=746749378,appkey=172140270,method=getFansListByFanPropertyAndTagCondi,classId=718,page=1,pageSize=100,propertyName=life_cycle,propertyValue=Mature+Consumer,sortFlag=True,sortPropertyName=interact,sortType=desc','http://211.151.58.219:10091/cdapi/req')