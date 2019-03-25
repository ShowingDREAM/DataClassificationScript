#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import zipfile
import time
import datetime
import os
import shutil
from glob import glob
import sys
global count
Address=sys.argv[1]
Address2=sys.argv[2]
Type=sys.argv[3]
def un_zip(filename):
        isZip = filename[filename.rfind("."):]
        if(isZip == ".zip"):
            try:
                    zip_file = zipfile.ZipFile(filename)
                    a_name=zip_file.namelist()
                    if (filename.find(".zip")) > -1:
                            zip_file = zipfile.ZipFile(filename)
                            a_name=zip_file.namelist()
                    else:
                            return
                    for names in a_name:
                            if (names.find(Type)) > -1:
                                    try:
                                            #print("-----find a file!")
                                            global count
                                            count+=1
                                            file_io.write(str(count)+' '+filename+'\n')
                                            #zip_file.extract(names,Address2) extract #the zipfile
                                    except:
                                            print("######"+filename+"Unzip Failed_X ?")
                                            pass
                    print ("######"+filename+"  Unzip Done_V")
            except:
                    pass
        else:
            return

def all_path(dirname):
    substr = dirname.rfind("\\")
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            #print("."+apath[substr:])
            Pos_zip = "."+apath[substr:]
            files = glob(Pos_zip)
            for file_name in files:
                un_zip(file_name)

def spendHour(time1,time2):
        print("\n========Time Message================")
        print("The start time %s" % time1)
        print("The end time   %s" % time2)
        spend=(time2-time1).seconds
        m,s=divmod(spend,60)
        h,m=divmod(m,60)
        print("Total time     [%d:%02d:%02d]" % (h, m, s))#时间差

start=datetime.datetime.now()#开始时间
file_io=open(Address2+'\Message.txt',mode='a+')
global count
count=0
all_path(Address)
file_io.close()
end=datetime.datetime.now()#结束时间

spendHour(start,end)#调用时间输出函数

print("\n========All File has finished================")
