# -*- coding: utf-8 -*-
#****************************************************************
# checkPoint.py
# Author     : hsn
# Version    : 1.0
# Date       : 2016-04-20
# Description:
#****************************************************************
import writeLog
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def assert_result(sReal, sExpect):
    """
    两个字符串对比
    sReal:实际结果
    sExpect:预期结果
    """
    sReal=str(sReal)
    sExpect=str(sExpect)
    if sReal==sExpect:
        print 'OK'
        writeLog.WriteLog('PASS')
    else:
        print 'NG'
        writeLog.WriteLog('FAIL')


def check_result(datas,Edatas,desc,Edesc,flag,Eflag,name):
    """
    验证结果
    datas：请求返回值
    Edatas：预期返回值
    desc：状态提示语
    Edesc：预期提示语
    flag：请求状态码
    Eflag：预期状态码
    num:用例编号
    """
    datas=str(datas)
    Edatas=str(Edatas)
    #desc=str(desc)
    #Edesc=str(Edesc)
    flag=str(flag)
    Eflag=str(Eflag)
    #num=str(num)
    name=str(name)
    #print datas
    #print Edatas

    if flag==Eflag:
        #print 'flag is right'
        if desc==Edesc:
            #print 'desc is right'
            if datas==Edatas:
                print 'same datas&desc&flag'
                writeLog.WriteLog(name+':'+'PASS:same datas&desc&flag')
                return True
            else:
                print 'FAIL:wrong datas'
                writeLog.WriteLog(name+':'+'FAIL:wrong datas','datas:'+datas+',Edatas:'+Edatas)
                return False
        else:
            print 'FAIL:wrong desc'
            writeLog.WriteLog(name+':'+'FAIL:wrong desc','desc:'+desc+',Edesc:'+Edesc)
            return False
    else:
        print 'FAIL:wrong flag'
        writeLog.WriteLog(name+':'+'FAIL:wrong flag','flag:'+flag+',Eflag:'+Eflag)
        return False

####################################################
if __name__ =='__main__':
    #assert_result(1,1)
    check_result('1','x','2','2','3','3','111')