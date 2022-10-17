import requests
from bs4 import BeautifulSoup as bs
import lxml
import time


def main():
    """Main function"""

    # Сбор ссылок на странички с полным текстом статей
    response = requests.get(url=url, params=useragent).text
    soup = bs(response, 'lxml')
    articles = soup.find_all(class_='tm-articles-list__item')
    links = []
    for article in articles:
        href = 'https://habr.com' + \
            article.find(class_="tm-article-snippet__title-link")['href']
        links.append(href)
    print(f'Собрано {len(links)} ссылок на статьи')

    # Сбор данных со страничек статей
    time.sleep(waiting)
    articles_data = []
    for num, link in enumerate(links, 1):
        print(f'Проверяем статью по ссылке {link}')
        response = requests.get(url=link, params=useragent).text
        soup = bs(response, 'lxml')
        article_text = soup.find(class_="article-formatted-body").text

        # Проверка ключевых слов
        for key in keywords:
            if key in article_text:
                date = soup.find(class_='tm-article-snippet__datetime-published').text
                title = soup.find(class_="tm-article-snippet__title tm-article-snippet__title_h1").find('span').text
                article_data = [date, title, link]
                articles_data.append(article_data)
                break

        print(f'Обработано {num} из {len(links)} статей ')
        time.sleep(waiting)

    print("Результат проверки наличия ключевых слов:")
    for article in articles_data:
        print(article)


if __name__ == '__main__':
    waiting = 1 # Time wait for next request
    keywords = ['дизайн', 'фото', 'web', 'python']
    url = 'https://habr.com/ru/all/'
    useragent = 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
    main()
