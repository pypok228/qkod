import requests
from bs4 import BeautifulSoup
import time
sleep = 10
def update_ticker():
    NVDA = "https://pb.nalog.ru/search.html#quick-result?regionUl=63&mode=search-ul&page=1&pageSize=10"
    headers = {
                'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                              "AppleWebKit/537.36 (KHTML, like Gecko)"
                              "Chrome/98.0.4758.102 Safari/537.36"}
    html = requests.get(NVDA, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    #convert = soup.find('div')
    stad = soup.find_all('span', class_="result-group-name")
    #fars = stad.find_all('div', class_='result-group')
    sf = soup.find_all('ЗАО "АКСАНД"')
    print(stad)
    time.sleep(sleep)
    update_ticker()


update_ticker()




