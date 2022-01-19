from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")  # folder for web drivers
driver.implicitly_wait(5)  # waiting time
driver.get("https://google.com")  # open web page

"""find element in source code name='q' (search field) and type 'naveen automation' """
driver.find_element(By.NAME, 'q').send_keys("naveen automation")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')  # find all prediction keywords
print("Found prediction keywords:", len(optionsList))  # print amount of prediction keywords

for ele in optionsList:  # print all prediction keywords
    print(ele.text)
    if ele.text == "naveen automation labs youtube":  # click on this keyword
        ele.click()
        break  # break the loop

# click on predictions keywords

print("Key was sent to >", driver.title)  # what to do

time.sleep(2)  # close browser after secs
driver.quit()

"""
# lesson https://www.youtube.com/watch?v=86nEglbjvIk
"""