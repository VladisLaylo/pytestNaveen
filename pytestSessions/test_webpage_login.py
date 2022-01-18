from selenium import webdriver
from selenium.webdriver import ActionsChains
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.google.com')
    assert driver.title == "Google"
    time.sleep(1)
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com')
    assert driver.title == "Facebook - log in or sign up"
    time.sleep(1)
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.instagram.com')
    assert driver.title == "Instagram"
    time.sleep(1)
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.gmail.com')
    assert driver.title == "Gmail"
    time.sleep(1)
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.rediff.com')
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    time.sleep(1)
    driver.quit()
