from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://vladis03.bugfocus.com/numberprovisioning/provider/")

# driver.find_element(By.CSS_SELECTOR, '#username').send_keys("admin")
driver.find_element(By.CLASS_NAME, 'ui input').send_keys("admin")

driver.find_element(By.NAME, 'password').send_keys("password")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.ui.fluid.primary.button._9KiXtv4-sIyPsj0NCycBi.nsNrtkvKxNxggQKoZjiWM').click()

time.sleep(2)
driver.quit()

"""
pytest LocatorsCSSCLASSName.py

How to create CSS_SELECTOR if not present?

1) if ID="username" is available put # in front name of ID to convert it to (By.CSS_SELECTOR, '#username'), 

2) if class="ui fluid primary button _9KiXtv4-sIyPsj0NCycBi nsNrtkvKxNxggQKoZjiWM"

2.1) replace all spaces in class by dots '.' and put dot infront, 
e.g. ".ui.fluid.primary.button._9KiXtv4-sIyPsj0NCycBi.nsNrtkvKxNxggQKoZjiWM"

2.2) if doesn't work and put "input" in front 
e.g. "input.ui.fluid.primary.button._9KiXtv4-sIyPsj0NCycBi.nsNrtkvKxNxggQKoZjiWM"

"""