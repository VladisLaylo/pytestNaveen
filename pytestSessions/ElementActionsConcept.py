from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://classic.crmpro.com/')

username_ele = driver.find_element(By.NAME, 'username')
password_ele = driver.find_element(By.NAME, 'password')
login_button_ele = driver.find_element(By.XPATH, "//input[@type='submit']")

act_chains = ActionChains(driver)
act_chains.send_keys(username_ele, 'batchautomation').perform()
act_chains.send_keys(password_ele, 'Test@12345').perform()
act_chains.click(login_button_ele)


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