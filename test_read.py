def readTheTxt(address):
    file = open(address)
     
    while 1:
        line = file.readline()
        if not line:
            break #end
        line = line.strip('\n')#ȥ�س�
        line=line[line.find("."):]#ȥ�ײ�
        line=line.replace("\\","\\\\")#�滻�»���
        print(line) # do something
readTheTxt("C:\\CSDN\\apk.txt")
