import os
import json
rootdir = 'C:\\Users\\sisi\\Desktop\\�½��ļ���\\ResultTxt3'
       
def loadresponse(pathh):
       f=open(pathh)
       textfile=json.load(f)
       if(textfile['response_code']!=1):
           writeMessage(textfile['resource'])
       return textfile['response_code']
def writeMessage(sha256):
       file_io=open('upLoadFile.txt',mode='a+')
       file_io.write(sha256+'\n')
       file_io.close()
list = os.listdir(rootdir) #�г��ļ��������е�Ŀ¼���ļ�
count=1
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       if os.path.isfile(path):
              address=os.path.abspath(path)#����·��
              loadresponse(address)
              print(count)
              count=count+1
