import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://spicejet.com")

'''move to element'''
add_ons_ele = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[1]/div[2]/div[1]/div/div[2]/div['
                                        '1]/div/div[1]/div[1]')
act_chains = ActionChains(driver)
act_chains.move_to_element(add_ons_ele).perform()

seat_meal_ele = driver.find_element(By.LINK_TEXT, 'Seat + Meal Combo')
act_chains.move_to_element(seat_meal_ele).perform()
time.sleep(2)
seat_meal_ele.click()

time.sleep(5)
driver.quit()

'''
Part of the lesson:
https://youtu.be/pFLmQ4Vo9Co
RightClickMouse.py
ElementActionsConcept.py
MoveToElementConcept.py
DragAndDrop.py
'''