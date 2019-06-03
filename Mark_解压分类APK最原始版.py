import json
import urllib 
import urllib2
import os
import zipfile
import sys

TXTADDRESS="C:\AB\\apk.txt"
TARGET="C:\AB\\ss"
apikey="c0589a92e5297b5f0247c7e82ce147eab690b612c5705748d77dc754c371693a"	#vt�˺ŵ�key
url = "https://www.virustotal.com/vtapi/v2/file/report"

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
        path="G:\\samples"+line
        print(path) # do something
        #print(strmd5)
        VTextrect(strmd5,path)#����API����
def VTextrect(md5,src):
    param = {'resource':md5, 'apikey':apikey, 'allinfo': '1'}
    data = urllib.urlencode(param)
    result = urllib2.urlopen(url, data)
    q=result.read()
    if(q==""):
        print("Not exist in VT,it's new")
        #unzip_file(src,TARGET+"\\Uncertain")
        file_io.write(src+'\n')
        return   #������е��ļ�����VT���У����Բ��ᷴ���κζ���
    jsondata =  json.loads(q) 
    response_code=jsondata['response_code']
    if(response_code==0):
        print("Not exist in VT")
        unzip_file(src,TARGET+"\\Notin")
    if(response_code==1):
        #nameofsha256=jsondata['sha256']
        #print(nameofsha256)
        positives=jsondata['positives']
        if(positives==0):
            print("It'is Benign")
            unzip_file(src,TARGET+"\\Begin")
        else:
            print("It'is Malware")
            unzip_file(src,TARGET+"\\Malware")
    return
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
            print('Has Unpacked!')
    else:
        print('This is not zip')
#readTheTxt("C:\\CSDN\\bbb\\apk2.txt")#TET���ļ�·��
file_io=open('Uncertain.txt',mode='a+')
readTheTxt(TXTADDRESS)
file_io.close()
