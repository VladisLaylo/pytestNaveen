from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.get("http://demo.automationtesting.in/Alerts.html")

# driver.find_element(By.NAME, 'proceed').click()
driver.find_element(By.CSS_SELECTOR, '.btn.btn-danger').click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # accept it by clicking OK
# alert.dismiss()  # cancel the popup

driver.switch_to.default_content()  # driver return to page
# driver.switch_to_default_content()

time.sleep(3)
driver.quit()

'''
https://youtu.be/ttFg6mwWe7g
'''
