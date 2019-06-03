#本脚本对硬盘中的zip进行解压，，然后将解压的文件存到参数2的路径中，并且创建txt哈希值
#使用是时候，将本py文件和apk.txt文件放到一起既可以了
#参数1-TXTADDRESS：读取的txt地址，txt中存放的是各个zip的路径
#参数2-TARGET：计算出的哈希值保存的路径
#参数3-为硬盘的前缀，和参数1一起构成一个完整的地址
#示例
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
        line = line.strip('\n')#去回车
        line=line[line.find(".")+1:]#去首部
        #line=line.replace("\\","\\\\")#替换下划线
        path=DISK+line
        file_io2.write("#"+path+'\n')
        print(path) # do something
        saveHashMessage(path)
        #print(strmd5)
        #VTextrect(strmd5,path)#进行API分析
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
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#时间差
#readTheTxt("C:\\CSDN\\bbb\\apk2.txt")#TET的文件路径
start=datetime.datetime.now()#开始时间
file_io=open('Hash.txt',mode='a+')
file_io2=open('HashAndPath.txt',mode='a+')
readTheTxt(TXTADDRESS)
file_io.close()
file_io2.close()
end=datetime.datetime.now()#结束时间

spendHour(start,end)#调用时间输出函数
print("\n========All File has finished================")
