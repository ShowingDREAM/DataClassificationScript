# -*- coding: cp936 -*-
#�ýű��Էֺ����TXT�����ƶ��ļ��������z������һ��ԴTXT�ļ�����һ����Ŀ�ķ�����ļ��е�ַ
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
        line = line.strip('\n')#ȥ�س�
        typeN=line[0]#��ȡ�ײ�����
        line=line[1:]#ȥ�ײ�
        line=line.replace("\\","\\\\")#�滻�»���
        #print(typeN+"    "+line) # do something
        try:
            copyFile(typeN,line)
        except:
            print("��ǰ���ƴ�������")
def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#ʱ���

start=datetime.datetime.now()#��ʼʱ��
global COUNT
COUNT=0
readTheTxt(SOURCE)
end=datetime.datetime.now()#����ʱ��

spendHour(start,end)#����ʱ���������

print("\n========All File has finished================")
