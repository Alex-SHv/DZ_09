from bs4 import BeautifulSoup
import requests

response = requests.get("https://minfin.com.ua/currency/nbu/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"type": "nbu", "class": "sc-1x32wa2-10 evFbid"})
    res = soup_list[0].find("p", {"class": "sc-1x32wa2-9 glerpA"})
    print(res.text)