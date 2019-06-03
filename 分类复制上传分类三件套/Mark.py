import json
import urllib 
import urllib2
import os
import sys
import time
import datetime

TXTADDRESS="HashAndPath1.txt"
apikey="c0589a92e5297b5f0247c7e82ce147eab690b612c5705748d77dc754c371693a"	#vt账号的key
url = "https://www.virustotal.com/vtapi/v2/file/report"

def readTheTxt(address):
    file = open(address)
    searchCount=0
    while 1:
        searchCount=searchCount+1
        line = file.readline()#暂时没有用
        line2 = file.readline()#路径
        line3 = file.readline()#哈希值
        if not line:
            break #end
        #strmd5=line[line.rfind("\\")+1:line.rfind(".")]
        line2 = line2.strip('\n')#去回车
        line2=line2[1:]#去首部的路径
        line3 = line3.strip('\n')#去回车
        line3=line3[1:]#去首部的哈希值
        print("第 "+str(searchCount)+" 哈希值")
        #print(line2)
        #print(line3) # do something
        try:
            VTextrect(line3,line2)#进行API分析
        except:
            file_ioE=open('Excep.txt',mode='a+')
            file_ioE.write("第 "+str(searchCount)+" 哈希值"+'\n')
            file_ioE.write(line3+'\n')
            file_ioE.close()
        finally:
            if searchCount%4 == 0: #1分钟查4次
                print("-------------------Now it is waiting----------------------")
                time.sleep(60)#睡眠时间 
def VTextrect(md5,src):
    param = {'resource':md5, 'apikey':apikey, 'allinfo': '1'}
    data = urllib.urlencode(param)
    result = urllib2.urlopen(url, data)
    q=result.read()
    if(q==""):
        print("The Api is request over")
        file_io.write("4"+src+'\n')
        return   #这里的有的文件不在VT库中，所以不会反悔任何东西
    jsondata =  json.loads(q) 
    response_code=jsondata['response_code']
    if(response_code==0):
        print("Not exist in VT")
        file_io.write("3"+src+'\n')
    if(response_code==1):
        #nameofsha256=jsondata['sha256']
        #print(nameofsha256)
        positives=jsondata['positives']
        if(positives==0):
            print("It'is Benign")
            file_io.write("1"+src+'\n')
        else:
            print("It'is Malware")
            file_io.write("2"+src+'\n')
    return
def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#时间差

start=datetime.datetime.now()#开始时间
file_io=open('Report1.txt',mode='a+')
readTheTxt(TXTADDRESS)
file_io.close()
end=datetime.datetime.now()#结束时间

spendHour(start,end)#调用时间输出函数

print("\n========All File has finished================")
