#course
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt  

url = "http://www.cbr.ru/scripts//XML_daily.asp?"

today = dt.today()
today = today.strftime("%d/%m/%Y") 

payload = {"date_req" : today} 

response = requests.get(url, params=payload) 

html = BeautifulSoup(response.content, "html.parser")


def getCourse(id):
 return html.find("valute",  {'id': id}).value.text