from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.smartprix.com/mobiles")

time.sleep(5) #initial load
last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    load_more = driver.find_element(By.XPATH, "//div[@class='sm-load-more']")
    driver.execute_script("arguments[0].scrollIntoView();", load_more)
    driver.execute_script("arguments[0].click();", load_more)

    time.sleep(5)
        # নতুন হাইট চেক করুন
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        print("নতুন কোনো প্রোডাক্ট লোড হচ্ছে না। স্ক্র্যাপিং শেষ।")
        break

    last_height = new_height
    print("loading new product...")

html=driver.page_source
with open('mobile.html', 'w', encoding='utf-8') as f:
    f.write(html)