from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\webdrivers\geckodriver.exe")

driver.get("https://youtube.com")
