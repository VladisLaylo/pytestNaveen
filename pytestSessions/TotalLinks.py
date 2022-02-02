from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
# driver.delete_all_cookies()
# driver.maximize_window()

driver.get('https://amazon.com')
# driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

"""
links_list = driver.find_elements(By.TAG_NAME, 'a')
print(len(links_list))  # count total links

for ele in links_list:
    link_text = ele.text
    print(link_text)  # print link text
    print(ele.get_attribute('href'))  # get url"""

image_list = driver.find_elements(By.TAG_NAME, 'img')  # find images
print(len(image_list))  # count total images

for ele in image_list:
    print(ele.get_attribute('src'))


driver.quit()
"""
pytest pytestSessions/TotalLinks.py
"""