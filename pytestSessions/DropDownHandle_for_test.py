import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider/')

# login
driver.find_element(By.ID, 'username').send_keys("admin")
driver.find_element(By.ID, 'password').send_keys("password")
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()

# select tenant
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[5]/div/div/div[2]/div/input').send_keys(
    'TenantOne')
driver.find_element(By.CSS_SELECTOR, 'div.selected.item').click()

# expand filters
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div/div/div[3]/div['
                              '1]/i').click()


# def test_expand_carriers(init_driver):  # expand CARRIERS menu to get the list of items
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/i').click()
drop_list = driver.find_elements(By.CSS_SELECTOR,
                                 'span.text')  # collect list of menu items then print
for ele in drop_list:
    print(ele.text)
    if ele.text == 'Carrier Common':  # find item to click
        ele.click()
        break

# def test_expand_carriers(init_driver):  # expand COUNTRIES menu to get the list of items
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/i').click()
drop_list = driver.find_elements(By.CSS_SELECTOR,
                                 'span.text')  # collect list of menu items then print
for ele in drop_list:
    print(ele.text)
    if ele.text == 'United States +1':  # find item to click
        ele.click()
        break

time.sleep(5)
driver.quit()

"""
    EXPAND_FILTERS = (By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[1]/div[1]/form/div[2]/div/div/div/div['
                                '3]/div[1]')
    EXPAND_CARRIER = (By.XPATH, '//*[@id="AdvancedSearchPopup"]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/i')
    TYPE_CARRIER = (By.XPATH, '//*[@id="AdvancedSearchPopup"]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/input')
    # GET_CARRIER_LIST = (By.CSS_SELECTOR, 'div.visible.menu.transition')
    GET_CARRIER_LIST = (By.CSS_SELECTOR, 'span.text')
"""
"""
Run with run
https://youtu.be/bdU0Hqggwjw
https://youtu.be/4RCirQF0xuA
"""
