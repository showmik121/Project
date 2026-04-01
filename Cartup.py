from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://cartup.com/category/sneakers_356")
time.sleep(5) # Initial load
old_height=driver.execute_script("return document.body.scrollHeight")
# print(height)

counter=1
while True:
    load_more=driver.find_element(By.XPATH, "/html/body/section[1]/div[2]/div[3]/div[3]/div[4]/button")
    if "Nothing" in load_more.text:
        print("Done loading ✅")
        break

    load_more.click()
    time.sleep(2)

html=driver.page_source
with open('cartup.html', 'w', encoding='utf-8') as f:
    f.write(html)