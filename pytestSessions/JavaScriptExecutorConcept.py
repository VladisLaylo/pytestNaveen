from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.in/")

"""click on menu item "Best Sellers"""
# create web element
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')

"""create red border around Best Sellers menu item"""
driver.execute_script("arguments[0].style.border = '3px solid red'", best_sellers)

# click on it
driver.execute_script("arguments[0].click();", best_sellers)


"""get the page title"""
title = driver.execute_script("return document.title;")
print(title)

"""refresh the page"""
# driver.execute_script("history.go(0);")

"""generate the alert"""
# driver.execute_script("alert('Alert Generated with JavaScript');")

"""driver get page all texts"""
# inner_text = driver.execute_script("return document.documentElement.innerText;")
# print(inner_text)

"""scroll bottom of the page"""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

"""scroll the page naturally until you find the element"""
find_laptops = driver.find_element(By.XPATH, "//h2[text()='Bestsellers in Video Games']")
driver.execute_script("arguments[0].scrollIntoView(true);", find_laptops)
driver.execute_script("arguments[0].style.border = '3px solid red'", find_laptops)


"""scroll the page naturally until you find the element"""
find_word = driver.find_element(By.LINK_TEXT, 'Facebook')
driver.execute_script("arguments[0].scrollIntoView(true);", find_word)
driver.execute_script("arguments[0].style.border = '3px solid red'", find_word)

"""scroll top of the page"""
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

"""send keys into search"""
driver.execute_script("document.getElementById('twotabsearchtextbox').value='macbook pro'")

print(driver.execute_script("return navigator.userAgent;"))


time.sleep(5)
driver.quit()
