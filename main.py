import requests
from bs4 import BeautifulSoup as bs
import lxml

def main():
    """Main function"""
    
    response = requests.get(url=url, params=useragent).text
    soup = bs(response, 'lxml')
    data = soup.


if __name__ == '__main__':
    keywords = ['дизайн', 'фото', 'web', 'python']
    url = 'https://habr.com/ru/all/'
    useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
    main()