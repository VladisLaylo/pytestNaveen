from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com")

# header_element = driver.find_element(By.TAG_NAME, "h1")
header_element = driver.find_element(By.XPATH, "/html/body/section[1]/div[2]/div/div[1]/h1")
print(header_element.text)

time.sleep(2)
driver.quit()

"""
pytest LocatorsTagName.py

html tag H1 selector:
"""
