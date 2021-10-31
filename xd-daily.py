import requests
import json
import os
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',"Referer":"https://xxcapp.xidian.edu.cn/site/ncov/xidiandailyup"}
data={"sfzx":'1','tw':'1','area':'陕西省 西安市 长安区','city':'西安市','province':'陕西省','address':'陕西省西安市长安区兴隆街道竹园三路西安电子科技大学南校区','geo_api_info':'{"type":"complete","position":{"Q":34.12618733724,"R":108.84139458550402,"lng":108.841395,"lat":34.126187},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":83,"isConverted":true,"status":1,"addressComponent":{"citycode":"029","adcode":"610116","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"雷甘路","streetNumber":"238号","country":"中国","province":"陕西省","city":"西安市","district":"长安区","township":"兴隆街道"},"formattedAddress":"陕西省西安市长安区兴隆街道竹园三路西安电子科技大学南校区","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}','sfcyglq':'0','sfyzz':'0','qtqk':'','ymtys':'0'}
username=os.environ["username"]
password=os.environ["password"]
url="https://xxcapp.xidian.edu.cn/uc/wap/login/check"
p1=requests.Session()
p2=p1.post(url,headers = headers,data={"username":username,"password":password},timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
p2=p1.post("https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save",headers=headers,data=data,timeout=10)
if(p2.status_code!=200):
    raise Exception('不明原因失败');
a=json.loads(p2.text)
print(a['m'])
