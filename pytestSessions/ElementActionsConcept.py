from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://classic.crmpro.com/')
time.sleep(4)

username_ele = driver.find_element(By.NAME, 'username')
password_ele = driver.find_element(By.NAME, 'password')
login_button_ele = driver.find_element(By.XPATH, "//input[@type='submit']")

act_chains = ActionChains(driver)

act_chains.send_keys_to_element(username_ele, 'batchautomation')  # no need .perform() with send_keys_to_element
act_chains.send_keys_to_element(password_ele, 'Test@12345')  # to avoid send keys multiple times
act_chains.click(login_button_ele).perform()

time.sleep(3)
driver.quit()

'''
Part of the lesson:
https://youtu.be/pFLmQ4Vo9Co
RightClickMouse.py
ElementActionsConcept.py
MoveToElementConcept.py
DragAndDrop.py
'''
