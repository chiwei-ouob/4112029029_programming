import requests
import csv
import time
from bs4 import BeautifulSoup

url = 'https://search.books.com.tw/search/query/key/人工智慧/cat/all'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def parse_html(response):
    if response.status_code == requests.codes.ok:
        response.encoding = 'utf8'
        soup = BeautifulSoup(response.text, "html.parser")
    else: 
        print("HTTP Request Error")
        soup = None
    return soup

def save_to_csv(items, file):
    with open(file, 'w+', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for item in items:
            writer.writerows(item)

def web_scraping_bot():
    book_list = [['書名', '網址', '書價']]
    soup = parse_html(requests.get(url, headers=headers))
    if soup != None:
      # print("has soup")
      tag_item = soup.find_all(class_='table-td')
      # print(tag_item)
      # print("check1")
      i=1
      for item in tag_item:
        # print("check")
        book = []
        book.append(item.find("img")["alt"])
        book.append("http:" + item.find("a")["href"])
        price = item.find(class_="price").find_all("b")

        if len(price) == 1:
            book.append(price[0].string)
        else:
            book.append(price[1].string)
        # print(book)
        book_list.append(book)
        # print("sleeping...")
        time.sleep(2)
        i+=1
        if i==5: break
    else: print("No Soup")
    return book_list

if __name__ == '__main__':
    book_list = web_scraping_bot()
    for item in book_list:
        print(item)
    save_to_csv(book_list, "book_list.csv")