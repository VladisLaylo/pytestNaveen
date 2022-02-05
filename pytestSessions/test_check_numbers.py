import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

"""
def select_values(options_list, value):
    for ele in list_of_numbers:
        print(ele.text)
        for k in range(len(value)):
            if ele.text == value[k]:
                ele.click()
                break
                
"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider')
time.sleep(2)

driver.find_element(By.ID, 'username').send_keys("admin")
driver.find_element(By.ID, 'password').send_keys("password")
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@class="search"]').send_keys('Example Inc')
driver.find_element(By.XPATH, '//*[@class="search"]').send_keys(Keys.ENTER)


time.sleep(5)
driver.quit()
