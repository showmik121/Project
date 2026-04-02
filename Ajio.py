from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize driver correctly
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.ajio.com/men-backpacks/c/830201001")
time.sleep(2)  # Give Ajio time to load the initial grid

# Initialize height locally
last_height = driver.execute_script("return document.body.scrollHeight")
counter = 1

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new products to load (Ajio can be slow)
    time.sleep(5)

    # Calculate new scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # print(f"Scroll Count: {counter}")
    # counter += 1

    # Check if we have reached the end
    if new_height == last_height:
        print("Done: Reached the end of the page.")
        break

    last_height = new_height

html=driver.page_source
with open('Ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)