from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

"""options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.implicitly_wait(10)"""

driver.get("http://amazon.in")
print(driver.title)

"""
https://youtu.be/I4mEVhn95M8
"""
