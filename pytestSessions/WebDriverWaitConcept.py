from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://app.hubspot.com/login")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

# not working
wait = WebDriverWait(driver, 5)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))  # extra brackets!!!
email_id.send_keys('admin@admin.com')

'''
https://youtu.be/u5_uKZN0u7M

ec:
Different types of ExpectedConditions for Explicit wait:
title_is
title_contains
url_contains
url_to_be
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

'''
