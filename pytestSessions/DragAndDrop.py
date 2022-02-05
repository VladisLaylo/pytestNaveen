from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source_ele = driver.find_element(By.ID, 'draggable')
target_ele = driver.find_element(By.ID, 'droppable')

act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source_ele, target_ele).perform()  # single action works same
act_chains.click_and_hold(source_ele).move_to_element(target_ele).release().perform()

time.sleep(5)
driver.quit()

'''
https://youtu.be/pFLmQ4Vo9Co
'''