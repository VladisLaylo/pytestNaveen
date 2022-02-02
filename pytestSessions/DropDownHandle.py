import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')


ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[2]/div/a').click()  # accept cookies


def select_values(element, value):  # method to select value
    select = Select(element)
    select.select_by_visible_text(value)


def select_value_from_dropdown(drop_down_options_list, value):  # GENERIC METHODS For any list
    print(len(drop_down_options_list))
    for ele in drop_down_options_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


country_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
select_value_from_dropdown(country_options, 'United States')

"""
country_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
print(len(country_options))

for ele in country_options:
    print(ele.text)
    if ele.text == 'Russian Federation':
        ele.click()
        break
"""


"""
select_values(ele_country, 'United States')

# print all values from dropdown menu

select = Select(ele_country)
countries_list = select.options  # find complete list of options

for ele in countries_list:  # find menu item named Russian Federation, then break
    print(ele.text)
    if ele.text == 'Russian Federation':
        ele.click()
        break
        
print(len(countries_list))
"""


"""
# DIRECT METHODS
ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
select = Select(ele_country)  # after your get the methods select.*
select.select_by_visible_text("United States")

select.select_by_index(5)
select.select_by_value('Zimbabwe')
print(select.is_multiple)  # is the multiple select dropdown?
"""

time.sleep(2)
driver.quit()

"""
Run with run
https://youtu.be/4RCirQF0xuA
"""