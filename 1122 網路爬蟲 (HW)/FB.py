import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-notifications')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/nchumis')
time.sleep(5)

exit_btn = driver.find_element(By.XPATH, 
                               "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")

exit_btn.click()

for x in range(1, 6):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

if soup != None:
      tag_item = soup.find_all(class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a')
      i=1
      for item in tag_item:
        print (f"{i}.",f"\n   ".join(str(text.string) for text in item.find_all("div")))  # 或使用 .get_Text()
        time.sleep(2)
        i+=1