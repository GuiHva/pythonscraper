import bs4
import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r = requests.get('https://www.baidu.com/')
    r.encoding = 'utf-8'
    text = r.text
    soup = bs4.BeautifulSoup(text, 'html.parser')
    print(soup.prettify())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
