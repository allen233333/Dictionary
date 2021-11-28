import requests
while True:
    result = requests.get('http://dict-co.iciba.com/search.php?word='+input("search:"))#Dictioinary API
text = result.text
text = text.encode('utf8').decode("utf8")#Using Crawler to get the information of dictionary，and name the variable called“text”
print(text)
import re
patten=re.compile("\.&nbsp;&nbsp;(.*?)&nbsp;&nbsp")#using the correct expression: ”（. *?)"
result=patten.findall(text)
print (result)#print out
