from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

user_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_Name')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
phone_number = driver.find_element(By.ID, 'Form_submitForm_Contact')
platform_link = driver.find_element(By.LINK_TEXT, 'Platform')

user_url.send_keys('https://google.ru')
first_name.send_keys('Man')
email.send_keys('manman@yandex.ru')
phone_number.send_keys('16425148951')
platform_link.click()

time.sleep(2)
driver.quit()

"""
pytest LocatorsConcept.py -v --capture=tee-sys --html=LocatorsConcept_report.html
"""
