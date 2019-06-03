#coding=utf-8
import json
import urllib 
import urllib2
 
apikey="c0589a92e5297b5f0247c7e82ce147eab690b612c5705748d77dc754c371693a"	#vt账号的key
url = "https://www.virustotal.com/vtapi/v2/file/report"
md5 = "3a8f94ac5b0dd3c19fd51e79512f632a"					#样本MD5值
 
param = {'resource':md5, 'apikey':apikey, 'allinfo': '1'}
data = urllib.urlencode(param)
result = urllib2.urlopen(url, data)
jsondata =  json.loads(result.read())

response_code=jsondata['response_code']
print(response_code)
nameofsha256=jsondata['sha256']
print(nameofsha256)
positives=jsondata['positives']
print(positives)
total=jsondata['total']
print(total)
print("---------------------------------")
#print(jsondata)
file=open("./report.txt", "w")
json.dump(jsondata, file, indent=4)
file.close()
