import requests
from bs4 import BeautifulSoup
from abcdmy import *
from threading import Thread

def main ():
  url = 'https://finviz.com/screener.ashx'
  ds = get_all_the_contents (6, url)
  file = open ('b.txt', 'w')
  for d in ds:
      file.write (d['ticker'])
      file.write (' ')
      file.write (d['title'])
      file.write (' ')
      file.write (d['Price'])
      file.write ('\n')
  file.close ()




if __name__ == '__main__':
  main ()