import requests
from bs4 import BeautifulSoup


def get_html (url):
  r = requests.get (url)
  return r.text         ## возвращает html - код страницы

def parse_int_link (html):
  soup = BeautifulSoup (html, 'lxml')
  text = []
  valls = []
  vals = soup.find ('table', class_="snapshot-table2").find_all('td', class_="snapshot-td2")
  for val in vals:
    a = val.text
    valls.append (a)
  tds = soup.find ('table', class_="snapshot-table2").find_all('td', class_="snapshot-td2-cp")
  for td in tds:
    a = td.text
    text.append (a)
  d =  dict()
  length =  len(tds)
  for i in range (length):
    d[text[i]] = valls[i]
  print (d)

def get_all_links (html):
  soup = BeautifulSoup (html, 'lxml')
  tds = soup.find_all('a', class_='screener-link') # ищет все штуки вида <a href="..." class="screener-link">
  links = []
  link = 'https://finviz.com/'
  for td in tds:
    a = td.get('href') # собственно получает ссылку
    links.append (link + a)
  return links

def main ():
  url = 'https://finviz.com/screener.ashx'

  all_links = get_all_links (get_html (url))

  for i in all_links:
    parse_int_link (get_html (i))




if __name__ == '__main__':
  main ()