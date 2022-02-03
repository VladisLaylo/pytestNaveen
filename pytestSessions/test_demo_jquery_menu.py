from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import pyautogui
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://vladis01.bugfocus.com/sysmgmt')

sp_copyright = driver.find_element(By.XPATH, "//div[text()='Service Provider Login']")
print("Service Provider Login message present: " + sp_copyright.text)

driver.find_element(By.NAME, 'login').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys("password")
driver.find_element(By.CLASS_NAME, 'x-btn-text').click()
print("You are logged in")

time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Tenants']").click()
print("You are on Tenants page before add tenant")

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="gwt-debug-addTenantButton"]/tbody/tr[2]/td[2]/em/button').click()

time.sleep(2)
#  expand default language menu to get the list of items
driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[5]/div[1]/div/img').click()

drop_list = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
for ele in drop_list:
    print(ele.text)
    if ele.text == 'Dutch - Netherlands':  # find item to click
        ele.click()
        break


time.sleep(5)
driver.quit()

"""
https://youtu.be/bdU0Hqggwjw
"""