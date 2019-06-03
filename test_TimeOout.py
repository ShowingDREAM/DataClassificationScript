# coding=utf-8
import threading   
import json
import urllib 
import urllib2
import os
import sys
import time
import datetime

TXTADDRESS="Hash1.txt"
REPORTADDRESS=".//ResultTxt1//"
EXCEPTFILE="Excep1.txt"
apikey="c0589a92e5297b5f0247c7e82ce147eab690b612c5705748d77dc754c371693a"
url = "https://www.virustotal.com/vtapi/v2/file/report"
    
def readTheTxt(address):
    file = open(address)
    searchCount=0
    while 1:
        searchCount=searchCount+1
        line3 = file.readline()
        if not line3:
            break 
        line3 = line3.strip('\n')
        print("The "+str(searchCount)+" file")
        #print(line3) 
        
        t = threading.Thread(target=VTextrect(line3))#excute the fun
        t.setDaemon(True)
        t.start()
        t.join(15)
        if searchCount%4 == 0: 
            print("-------------------Now it is waiting----------------------")
            time.sleep(60)
def VTextrect(md5):
    try:
        param = {'resource':md5, 'apikey':apikey, 'allinfo': '1'}
        data = urllib.urlencode(param)
        result = urllib2.urlopen(url, data)
        q=result.read()
        if(q==""):
            print("The Api is request over Time")
            file_ioE=open(EXCEPTFILE,mode='a+')
            file_ioE.write(md5+'\n')
            file_ioE.close()
            return  
        jsondata =  json.loads(q) 
        print("Result Has Saved")
        file=open(REPORTADDRESS+md5+".txt", "w")
        json.dump(jsondata, file, indent=4)
        file.close()
    except:
        print("The URL is Wrong")
        file_ioE=open(EXCEPTFILE,mode='a+')
        file_ioE.write(md5+'\n')
        file_ioE.close()
    return
def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#

start=datetime.datetime.now()#

if not os.path.exists(REPORTADDRESS):
    os.makedirs(REPORTADDRESS)
readTheTxt(TXTADDRESS)
end=datetime.datetime.now()#

spendHour(start,end)#

print("\n========All File has finished================")
