def readTheTxt(address):
    file = open(address)
     
    while 1:
        line = file.readline()
        if not line:
            break #end
        line = line.strip('\n')#去回车
        line=line[line.find("."):]#去首部
        line=line.replace("\\","\\\\")#替换下划线
        print(line) # do something
readTheTxt("C:\\CSDN\\apk.txt")
