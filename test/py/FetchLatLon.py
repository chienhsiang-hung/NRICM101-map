import requests
from bs4 import BeautifulSoup
import pandas as pd
import geocoder

def get_address():
    # 「清冠一號動態表」 : 公費清冠一號優先提供年長者及高風險族群 (供全台灣民眾查詢)
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml'
    resp = requests.get(url).text
    print(resp)
    soup = BeautifulSoup(resp, 'html.parser')
    print(soup.beautify())
    # soup = soup.table
    # pd.read_html(soup.table, encoding='utf-8')[0]
    
    
    print(pd.read_html(soup.find_all('table')[0], encoding='utf-8')[0])

def get_latlon(address:str):
    url = 'https://www.google.com/maps/place/' + address
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    resp = requests.get(url, headers=headers)
    print( resp.status_code)
    resp = resp.text
    print( resp )
    resp = resp[ resp.find('ll=') + 3 :]
    latlon = resp[: resp.find('"')]
    latlon = latlon.split(',')
    latlon = [float(num) for num in latlon]
    return latlon


if __name__ == '__main__':
    # print( get_latlon('台中市南屯區忠勇路27-3號') )
    # get_address()
    print(geocoder.google('台中市南屯區忠勇路27-3號').latlng)