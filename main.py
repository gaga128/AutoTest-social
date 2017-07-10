# -*- coding: utf-8 -*-
#****************************************************************
# main.py
# Author     : JIA
# Version    : 1.0
# Date       : 2016-05-20
# Description: 测试组装，用例执行入口
#****************************************************************
import os
import writeExcelresult
import sendReport
import getAutoCasesResults
import getCasesResults
import getTypeResults
import Execution
import readAllExcels

#接口测试
#设置测试用例
casesheet='Sheet2'                 ##手动生成case的sheetname
caseresult='CaRe'
Defaultsheet='Default parameter'  ##自动生成case的sheetname
Autocaseresult='AutoCaRe'
Autotyperesult='AutotypeCaRe'
Speparamlist=['','&#@￥%……','451264']     ##参数值为空、特殊字符和不存在的
typelist=[1, 15.5, 'string', False]


#testsuite begin
def Singlerun(casepath):
	runFirstresult = getCasesResults.runcase(casepath, casesheet, caseresult)  ####手动配置case生成case结果及对比
	Execution.Executionmode(runFirstresult,casepath,casesheet, caseresult)

	runFirstnullresult = getAutoCasesResults.createcase(casepath, Defaultsheet, Autocaseresult,Speparamlist)  ####自动生成case结果及对比
	Execution.Executionmode1(runFirstnullresult,casepath,Autocaseresult)

	runresult = getTypeResults.createtypecase(casepath, Defaultsheet, Autotyperesult, typelist)
	Execution.Executionmode2(runresult,casepath, Autotyperesult)


def runAll(allCasepath):
	filelist = readAllExcels.readfile(allCasepath)
	for i in range(0, len(filelist)):
		testcase=filelist[i]
		casepath=allCasepath+testcase
		runFirstresult = getCasesResults.runcase(casepath, casesheet, caseresult)  ####手动配置case生成case结果及对比
		Execution.Executionmode(runFirstresult, casepath, casesheet,caseresult)

		runFirstnullresult = getAutoCasesResults.createcase(casepath, Defaultsheet, Autocaseresult,Speparamlist)  ####自动生成case结果及对比
		Execution.Executionmode1(runFirstnullresult, casepath, Autocaseresult)

		runresult = getTypeResults.createtypecase(casepath, Defaultsheet, Autotyperesult, typelist)
		Execution.Executionmode2(runresult, casepath, Autotyperesult)
def email():
    sendReport.sendEmail()


###########################################################################单个用例和全部用例不能同时进行
if __name__=='__main__':
	# runAll(os.getcwd() + r'/mycase/')                  #########路径下全部测试用例
	Singlerun(os.getcwd()+r'/mycase/demo.xls')       ########路径下单个测试用例
	# email()

