from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider/')
driver.find_element(By.ID, 'username').send_keys("admin")
driver.find_element(By.ID, 'password').send_keys("password")
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[5]/div/div/div[2]/div/i').click()
time.sleep(5)


'''
https://youtu.be/ttFg6mwWe7g
'''