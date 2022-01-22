from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get("https://vladis01.bugfocus.com/sysmgmt")
driver.find_element(By.NAME, 'login').send_keys("admin")
driver.find_element(By.NAME, 'password').send_keys("password")
driver.find_element(By.CLASS_NAME, 'x-btn-text').click()
print("You are logged in")


time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Tenants']").click()
print("You are on Tenants page before add tenant")

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="gwt-debug-addTenantButton"]/tbody/tr[2]/td[2]/em/button').click()

driver.find_element(By.ID, 'gwt-debug-newName-input').send_keys("tenant-one-admin")  # Name
driver.find_element(By.ID, 'gwt-debug-newUrl-input').send_keys("tenant-one.bugfocus.com")  # Access domain
driver.find_element(By.ID, 'gwt-debug-newSip-input').send_keys("tenant-one-sip.bugfocus.com")  # SIP domain

driver.find_element(By.XPATH, '//*[@id="x-auto-106"]').click()  # Click to expand Region menu
driver.find_element(By.ID, 'x-auto-105-input').send_keys("Default")  # Region: select ID=x-auto-106
driver.find_element(By.ID, 'gwt-debug-newLoginId-input').send_keys("tenant-one-admin")  # Username
driver.find_element(By.ID, 'gwt-debug-newPassword-input').send_keys("password")  # Password
driver.find_element(By.ID, 'gwt-debug-newFirstName-input').send_keys("Tenant")  # First name
driver.find_element(By.ID, 'gwt-debug-newLastName-input').send_keys("One")  # Last name
driver.find_element(By.ID, 'gwt-debug-newEmail-input').send_keys("t1@brightpattern.com")  # Email

driver.find_element(By.ID, 'gwt-debug-newMaxConcurrentUsers-input').send_keys("10")  # Max users

driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # CLick to expand Database

# pyautogui.moveRel(0, 25)
pyautogui.click(700, 835)

"""driver = webdriver.Chrome(ChromeDriverManager().install())

action = webdriver.ActionChains(driver)

element = driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]')
action.move_to_element(element).perform()
action.move_by_offset(0, 25)    # 10px to the right, 20px to bottom
action.perform()
driver.click()"""

time.sleep(2)
driver.quit()
