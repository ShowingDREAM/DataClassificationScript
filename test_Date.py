import time
import datetime
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print("===============================================")
start=datetime.datetime.now()
print("时间是 %s" % start)
time.sleep(5)
end=datetime.datetime.now()
print("当前时间是 %s" % end)
spend=(end-start).seconds
print("时间间隔是 %s" % spend)
print("===============================================")
ss=360000.0
m,s=divmod(spend,60)
h,m=divmod(m,60)
print("%d:%02d:%02d" % (h, m, s))#时间差