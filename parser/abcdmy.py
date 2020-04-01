import requests
from bs4 import BeautifulSoup

def get_html (url):
  r = requests.get (url)
  return r.text         ## возвращает html - код страницы


def get_all_links (html):
  soup = BeautifulSoup (html, 'lxml')
  tds = set()
  tds = soup.find_all('a', class_='screener-link-primary') # ищет все штуки вида <a href="..." class="screener-link-primary">
  links = set ()
  link = 'https://finviz.com/'
  for td in tds:
    a = td.get('href') # собственно получает ссылку
    links.add (link + a)
  return links


def get_all_the_contents(num, url):
  a = -21
  d = []
  b = "?v=111&f=fa_debteq_u0.5,fa_epsyoy_pos,fa_pb_u3,fa_pc_low,fa_pe_low,fa_pfcf_low,fa_ps_u3&ft=2&r="
  for i in range (num):
    a = a + 20
    all_links = get_all_links (get_html (url + b + str (a)))
    for i in all_links:
      d.append (parse_int_link (get_html (i)))
  return d

def parse_int_link (html):
  soup = BeautifulSoup (html, 'lxml')
  title = soup.find ('title')
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
  txt = title.get_text ()
  txt = txt.split (' ')
  d['ticker'] = txt[0];
  txt.remove (txt[0])
  texxt = ''
  for tx in txt:
    texxt = texxt + tx + ' '
  d['title'] = texxt
  return d

#url = 'https://finviz.com/quote.ashx?t=A&ty=c&p=d&b=1'

#r = requests.get (url)

#soup = BeautifulSoup (r.text, 'lxml')
#with open('a.txt', 'w') as file:
 # file.write (soup.prettify())