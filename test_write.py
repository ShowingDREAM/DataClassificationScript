ii=0
file_io=open('Message.txt',mode='a+')
for i in range(5):
    file_io.write(str(ii)+str(i)+'hello word \n')
    ii+=1
file_io.close()
print("he")
