import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# url = 'http://127.0.0.1:5500/Final_Project/index.html'
# web = requests.get(url)                        # 取得網頁內容
# soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
# print(soup.find_all('div', id="NewsList"))

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
# 假的 headers 資訊
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# 加入 headers 資訊
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find('table', {'data-test':"historical-prices"})

data = []
rows = table.find_all('tr')
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
df = pd.DataFrame(data, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']).dropna()

plt.figure(figsize=(10, 6))
plt.plot(df['Close'].astype(float), label='Close Price')
plt.title('Apple Historical Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# plt.figure(figsize=(10, 6))
# plt.plot(df['Open'].astype(float), label='Open Price')
# plt.title('Yahoo Historical Open Stock Price')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.legend()
# plt.show()