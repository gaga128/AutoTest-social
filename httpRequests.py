# -*- coding: utf-8 -*-
#****************************************************************
# httpRequests.py
# Author     : hsn
# Version    : 1.0
# Date       : 2016-04-20
# Description:
#****************************************************************
import urllib2
import urllib

def URLreturn(httpString,porv):
    """
    返回url
    httpString:表1中接口url前缀
    params:参数列表，xlrd从excel单元格中定位
    """
    try:
        url = httpString + urlcode(porv)
        #print 'url:'+url
        return url
    except Exception, e:
        print e


def httpRequests(httpString,porv,methods):
    """
    封装请求
    httpString:表1中接口url前缀
    params:参数列表，xlrd从excel单元格中定位
    methons:采用POST还是GET方法
    """
    if methods == 'GET':
        try:
            url = httpString + urlcode(porv)
            #print 'geturl:'+url
            req = urllib2.Request(url)
            result = urllib2.urlopen(req).read().decode("UTF-8")
            #print 'get:',result
            return result
        except Exception, e:
            print e

    if methods == 'POST':
        try:
            url = httpString
            #print porv
            values = '{'+porv+'}'
            a = eval(values)                #改为字典mapping object型
            data = urllib.urlencode(a)
            #print 'data='+data
            req = urllib2.Request(url, data)
            #print req
            response = urllib2.urlopen(req)
            result = response.read().decode('UTF-8')
            #print 'post',result
            return result
        except Exception, e:
            print e


def urlcode(data):
    """
    url特殊字符编码转换
    空格变加号
    """
    if data.find('%3D'):            #处理等号
        data = data.replace('%3D','=')
        return data
    elif data.find('%26'):          #处理&符号
        data = data.replace('%26','&')
        return data
    else:                           #处理空格
        return urllib.quote_plus(data)


################################################################################
if __name__ == '__main__':
    a = httpRequests('http://211.151.58.219:10091/cdapi/req','"statisPropertyName":"interact","appid":"444","passwd":"746749378","method":"getFansNumOfGroupFieldByPropertyCon","appkey":"172140250","propertyName":"life_cycle","startTime":"1","endTime":"1555555555","propertyValue":"Mature+Consumer"','POST')#测试
    #a = urlcode('statisPropertyName%3Dinteract')
    print a

