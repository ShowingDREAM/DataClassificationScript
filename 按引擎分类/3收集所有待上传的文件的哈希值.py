import os
import json
rootdir = 'C:\\Users\\sisi\\Desktop\\新建文件夹\\ResultTxt3'
       
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
list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
count=1
for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       if os.path.isfile(path):
              address=os.path.abspath(path)#绝对路径
              loadresponse(address)
              print(count)
              count=count+1
