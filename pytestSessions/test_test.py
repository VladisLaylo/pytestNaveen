from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import pyautogui
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    # print("------------setup------------")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    # print("----------tear down----------")
    time.sleep(5)
    # driver.quit()


def test_sp_logo(init_driver):
    driver.get('https://vladis01.bugfocus.com/sysmgmt')
    sp_copyright = driver.find_element(By.XPATH, "//div[text()='Service Provider Login']")
    print("Service Provider Login message present: " + sp_copyright.text)


def test_login_into_sysmgmt(init_driver):
    driver.find_element(By.NAME, 'login').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("password")
    driver.find_element(By.CLASS_NAME, 'x-btn-text').click()
    print("You are logged in")


def test_open_tenants_page(init_driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Tenants']").click()
    print("You are on Tenants page before add tenant")


def test_add_new_tenant():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-addTenantButton"]/tbody/tr[2]/td[2]/em/button').click()


def test_fill_up_form_1(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newName-input').send_keys("Name")  # Name
    driver.find_element(By.XPATH, "//input[@id='gwt-debug-newUrl-input']").send_keys("Access domain")  # Access domain


def test_fill_up_form_2(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newSip-input').send_keys("SIP domain")  # SIP domain
    # driver.find_element(By.XPATH, '//*[@id="x-auto-106"]').click()  # Click to expand Region menu
    driver.find_element(By.ID, 'x-auto-105-input').send_keys("Default")  # Region: select ID=x-auto-106
    driver.find_element(By.ID, 'gwt-debug-newLoginId-input').send_keys("tenant-one-admin")  # Username
    driver.find_element(By.ID, 'gwt-debug-newPassword-input').send_keys("password")  # Password
    driver.find_element(By.ID, 'gwt-debug-newFirstName-input').send_keys("Tenant")  # First name
    driver.find_element(By.ID, 'gwt-debug-newLastName-input').send_keys("One")  # Last name
    driver.find_element(By.ID, 'gwt-debug-newEmail-input').send_keys("t1@brightpattern.com")  # Email

    driver.find_element(By.ID, 'gwt-debug-newMaxConcurrentUsers-input').send_keys("10")  # Max users

    # driver.find_element(By.XPATH, '//*[@id="x-auto-118"]').click()  # CLick to expand Database server menu
    # driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # CLick to expand Database
    # server menu
    # pyautogui.click(700, 835)


"""
def perform_click():
    pyautogui.click(700, 835)
"""


# class="x-form-trigger x-form-trigger-arrow form-trigger-over"


def test_finalise_form(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newDbName-input').send_keys("tenant_1_db")  # Database name
    driver.find_element(By.ID, 'gwt-debug-newDbUser-input').send_keys("tenant_1_usr")  # Username
    driver.find_element(By.ID, 'gwt-debug-newDbPassword-input').send_keys("password")  # Password
    # driver.find_element(By.XPATH, "//button[text()='OK']").click()  # Click on OK
    # driver.find_element(By.XPATH, '//*[@id="gwt-debug-confirmButton"]/tbody/tr[2]/td[2]').click()  # Click on OK""""""


"""
pytest test_sp_service_provider_add_tenant.py -v --capture=tee-sys --html=test_sp_service_provider_add_tenant.py.html

LIFE HACK
actions.move_to_element(element_to_select).perform()

In your case, to select something from the "Socks" menu:

e1 = driver.find_element_by_xpath('//*[@id="nav"]/ol/li[5]/a')
e2 = e1.find_element_by_xpath('../ul/li[1]/a')
actions.move_to_element(e1).move_to_element(e2).perform()
e2.click()

MOVE MOUSE
def test_to_select_db_server():

    a = ActionChains(driver)  # object of ActionChains
    m = driver.find_element_by_link_text("Enabled")  # identify element
    a.move_to_element(m).perform()  # hover over element
    n = driver.find_element_by_link_text("Back to JQuery UI") # identify sub menu element
    a.move_to_element(n).click().perform()  # hover over element and click

MOVE MOUSE
driver = webdriver.Firefox(executable_path=driver_path)
action = webdriver.ActionChains(driver)
element = driver.find_element_by_id('your-id') # or your another selector here
action.move_to_element(element)
action.perform()
action.move_by_offset(10, 20)    # 10px to the right, 20px to bottom
action.perform()
actions.move_to_element(element_to_select).perform()

MAKE MOUSE MOVE

import pyautogui

==============
MOISE MOVE GRATE!

pip install pyautogui

select one of the option you need: 

pyautogui.click(100, 100)
pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

???     pyautogui.click(x=300, y=300, clicks=3, interval=2, button='right')    

====================
MOVE MOUSE
import autopy # pip install autopy
autopy.mouse.smooth_move(100, 600)

"""
