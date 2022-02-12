from selenium import webdriver
from service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
'''
dynamic
global wait
find_element
find_elements
only for webelements

NOT APPLIED TO: non webelements, e.g. URLs, Title, Alerts etc
'''

driver.get('https://app.hubspot.com/login')

'''
https://youtu.be/ER5gpVt-0BU
'''