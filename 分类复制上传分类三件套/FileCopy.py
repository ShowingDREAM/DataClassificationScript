# -*- coding: cp936 -*-
#该脚本对分好类的TXT进行移动文件操作，倆参数，一个源TXT文件，另一个是目的分类的文件夹地址
#
import shutil
import os
import time
import datetime

SOURCE="C:\\MARK\\Exp\\result-apart\\HashAndPath1.txt"
TARGET="G:\\SETOFDATA\\Sample1"
path1 =TARGET+"\\Begin"
path2 =TARGET+"\\Malware"
path3 =TARGET+"\\Uncertain"
path4 =TARGET+"\\Overtime"
global COUNT
def makedirs():
    if not os.path.exists(path1):
        os.makedirs(path1)
    if not os.path.exists(path2):
        os.makedirs(path2)
    if not os.path.exists(path3):
        os.makedirs(path3)
    if not os.path.exists(path4):
        os.makedirs(path4)

def copyFile(typeN,address):
    global COUNT
    COUNT=COUNT+1
    print("The "+str(COUNT)+" is copying---")
    if(typeN=="1"):
        shutil.copy(address,path1)
    elif(typeN=="2"):
        shutil.copy(address,path2)
    elif(typeN=="3"):
        shutil.copy(address,path3)
    elif(typeN=="4"):
        shutil.copy(address,path4)
    else:
        return

def readTheTxt(address):
    file = open(address)
    makedirs()
    while 1:
        line = file.readline()
        if not line:
            break #end
        line = line.strip('\n')#去回车
        typeN=line[0]#获取首部数字
        line=line[1:]#去首部
        line=line.replace("\\","\\\\")#替换下划线
        #print(typeN+"    "+line) # do something
        try:
            copyFile(typeN,line)
        except:
            print("当前复制存在问题")
def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#时间差

start=datetime.datetime.now()#开始时间
global COUNT
COUNT=0
readTheTxt(SOURCE)
end=datetime.datetime.now()#结束时间

spendHour(start,end)#调用时间输出函数

print("\n========All File has finished================")
