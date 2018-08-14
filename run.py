import requests
import json
key = "378e38a2bf6e4d2f8bff88e4ad6170f7"
print("Ailie 正在运行")
while True:
	info = input("\n我：")
	url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
	res = requests.get(url)
	res.enconding = 'utf-8'
	jd = json.loads(res.text)
	print("\nAilie: "+jd['text'])