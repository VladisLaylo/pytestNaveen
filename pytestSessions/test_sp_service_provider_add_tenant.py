from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
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
    #driver.quit()


def test_sp_logo(init_driver):
    driver.get('https://vladis01.bugfocus.com/sysmgmt')
    sp_copyright = driver.find_element(By.XPATH, "//div[text()='Service Provider Login']")
    print("Service Provider Login message present: " + sp_copyright.text)


def test_login_into_sysmgmt():
    driver.find_element(By.NAME, 'login').send_keys("admin")
    driver.find_element(By.NAME, 'password').send_keys("password")
    driver.find_element(By.CLASS_NAME, 'x-btn-text').click()
    print("You are logged in")


def test_open_orders_page():
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Tenants']").click()
    print("You are on Tenants page before add tenant")


def test_add_new_tenant():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-addTenantButton"]/tbody/tr[2]/td[2]/em/button').click()

    driver.find_element(By.ID, 'gwt-debug-newName-input').send_keys("tenant-one-admin")  # Name
    driver.find_element(By.ID, 'gwt-debug-newUrl-input').send_keys("tenant-one.bugfocus.com")  # Access domain
    driver.find_element(By.ID, 'gwt-debug-newSip-input').send_keys("tenant-one-sip.bugfocus.com")  # SIP domain

    driver.find_element(By.XPATH, '//*[@id="x-auto-106"]').click()  # Click to expand Region menu
    driver.find_element(By.ID, 'x-auto-105-input').send_keys("Default")  # Region: select ID=x-auto-106
    driver.find_element(By.ID, 'gwt-debug-newLoginId-input').send_keys("tenant-one-admin")  # Username
    driver.find_element(By.ID, 'gwt-debug-newPassword-input').send_keys("password")  # Password
    driver.find_element(By.ID, 'gwt-debug-newFirstName-input').send_keys("Tenant")  # First name
    driver.find_element(By.ID, 'gwt-debug-newLastName-input').send_keys("One")  # Last name
    driver.find_element(By.ID, 'gwt-debug-newEmail-input').send_keys("t1@brightpattern.com")  # Email

    driver.find_element(By.ID, 'gwt-debug-newMaxConcurrentUsers-input').send_keys("10")  # Max users

    # driver.find_element(By.XPATH, '//*[@id="x-auto-118"]').click()  # CLick to expand Database server menu
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # CLick to expand Database
    # server menu
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # DB server:
    # select

    driver.find_element(By.ID, 'gwt-debug-newDbName-input').send_keys("tenant_1_db")  # Database name
    driver.find_element(By.ID, 'gwt-debug-newDbUser-input').send_keys("tenant_1_usr")  # Username
    driver.find_element(By.ID, 'gwt-debug-newDbPassword-input').send_keys("password")  # Password
    driver.find_element(By.XPATH, "//button[text()='OK']").click()  # Click on OK




"""
pytest test_sp_service_provider_add_tenant.py -v --capture=tee-sys --html=test_sp_service_provider_add_tenant.py.html

"""