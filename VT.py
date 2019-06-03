#coding=utf-8
import json
import urllib 
import urllib2
 
apikey="c0589a92e5297b5f0247c7e82ce147eab690b612c5705748d77dc754c371693a"	#vt账号的key
url = "https://www.virustotal.com/vtapi/v2/file/report"
md5 = "706af0b837daae706425cfb112c87be51bc50210c6a59ee747e15105bfa4e820"					#样本MD5值
 
param = {'resource':md5, 'apikey':apikey, 'allinfo': '1'}
data = urllib.urlencode(param)
result = urllib2.urlopen(url, data)
jsondata =  json.loads(result.read())
 
file=open("./report.txt", "w")
json.dump(jsondata, file, indent=4)
file.close()
