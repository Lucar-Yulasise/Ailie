import requests
import json
import pyttsx3


key = "378e38a2bf6e4d2f8bff88e4ad6170f7"
print("Ailie 正在运行")


def get_information(url):
	res = requests.get(url)
	res.enconding = 'utf-8'
	jd = json.loads(res.text)
	return jd['text']


def main():

	engine = pyttsx3.Engine()
	rate = engine.getProperty('rate')
	engine.setProperty('rate',200)

	while True:
		info = input("我：")
		url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
		word = get_information(url)


		print("艾莉: "+word)
		engine.say(word)
		engine.runAndWait()
		if info == "exit":
			engine.stop()
			exit(1)
		

if __name__=='__main__':
	main()

	