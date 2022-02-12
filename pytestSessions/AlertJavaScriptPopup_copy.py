from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://vladis03.bugfocus.com/numberprovisioning/provider")
driver.find_element(By.ID, 'username').send_keys('admin')
driver.find_element(By.ID, 'password').send_keys('password')
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()


driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[5]/div/div/div[2]/div/i').click()
drop_item = driver.find_elements(By.CSS_SELECTOR, 'div.item')
# collect list of menu items then print
for ele in drop_item:
    print(ele.text)
    if ele.text == 'All tenants':  # find item to click
        ele.click()
        break

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button').click()

'''alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # accept it by clicking OK
# alert.dismiss()  # cancel the popup'''

time.sleep(10)
driver.quit()

'''
https://youtu.be/ttFg6mwWe7g
'''
