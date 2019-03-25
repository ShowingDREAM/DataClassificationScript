import zipfile
import tarfile
import os
import shutil
from glob import glob
import sys
global count
Address=sys.argv[1]
Pos_unzip=sys.argv[2]
Type=sys.argv[3]
def un_zip(filename):
        isZip = filename[filename.rfind("."):]
        if(isZip != ".zip"):
            return
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
                                #zip_file.extract(names,Pos_unzip) extract #the zipfile
                        except:
                                print("######"+filename+"Unzip Failed_X ?")
                                pass
        print ("######"+filename+"  Unzip Done_V")
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
file_io=open('Message.txt',mode='a+')
global count
count=0
all_path(Address)
file_io.close()
print("\n========All File has finished================")