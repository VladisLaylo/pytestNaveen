import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def select_values(options_list, value):
    if not value[0] == 'all':
        for ele in drop_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        for ele in options_list:
            ele.click()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
time.sleep(2)

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')  # accept cookies
values_list = ['all']
select_values(drop_list, values_list)
