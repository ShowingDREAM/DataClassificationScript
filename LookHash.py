#���ű���Ӳ���е�zip���н�ѹ����Ȼ�󽫽�ѹ���ļ��浽����2��·���У����Ҵ���txt��ϣֵ
#ʹ����ʱ�򣬽���py�ļ���apk.txt�ļ��ŵ�һ��ȿ�����
#����1-TXTADDRESS����ȡ��txt��ַ��txt�д�ŵ��Ǹ���zip��·��
#����2-TARGET��������Ĺ�ϣֵ�����·��
#����3-ΪӲ�̵�ǰ׺���Ͳ���1һ�𹹳�һ�������ĵ�ַ
#ʾ��
#TXTADDRESS="G:\DATA\\apk.txt"
#TARGET="G:\DATA\\APKFile"
#DISK="I:\\samples"

import json
import urllib 
import urllib2
import os
import zipfile
import sys
import hashlib
import time
import datetime

TXTADDRESS="G:\DATA5\\disk26_apk.txt"
TARGET="G:\DATA5\\APKFile"
DISK="H:"
def readTheTxt(address):
    file = open(address)
     
    while 1:
        line = file.readline()
        if not line:
            break #end
        strmd5=line[line.rfind("\\")+1:line.rfind(".")]
        line = line.strip('\n')#ȥ�س�
        line=line[line.find(".")+1:]#ȥ�ײ�
        #line=line.replace("\\","\\\\")#�滻�»���
        path=DISK+line
        file_io2.write("#"+path+'\n')
        print(path) # do something
        saveHashMessage(path)
        #print(strmd5)
        #VTextrect(strmd5,path)#����API����
def saveHashMessage(src):
    unzip_file(src,TARGET)
def hashh(new_path):
    f = open(new_path,'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    nameSha256=sh.hexdigest()
    file_io.write(nameSha256+'\n')
    file_io2.write("@"+nameSha256+'\n')
    f.close()
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
            newpath=TARGET+"\\"+file
            file_io2.write("$"+newpath+'\n')
            hashh(newpath)
            print('Has Unpacked!')
    else:
        print('This is not zip')
        
def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#ʱ���
#readTheTxt("C:\\CSDN\\bbb\\apk2.txt")#TET���ļ�·��
start=datetime.datetime.now()#��ʼʱ��
file_io=open('Hash.txt',mode='a+')
file_io2=open('HashAndPath.txt',mode='a+')
readTheTxt(TXTADDRESS)
file_io.close()
file_io2.close()
end=datetime.datetime.now()#����ʱ��

spendHour(start,end)#����ʱ���������
print("\n========All File has finished================")
