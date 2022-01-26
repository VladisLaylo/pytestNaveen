from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import pyautogui
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("------------setup------------")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    yield
    print("----------tear down----------")
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


def test_click_add_new_tenant(init_driver):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-addTenantButton"]/tbody/tr[2]/td[2]/em/button').click()


def test_fill_up_form(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newName-input').send_keys("Tenant1")  # Name
    driver.find_element(By.XPATH, "//input[@id='gwt-debug-newUrl-input']").send_keys("t1.ru")  # Access domain
    # domain
    driver.find_element(By.ID, 'gwt-debug-newSip-input').send_keys("sip1.ru")  # SIP domain
    driver.find_element(By.XPATH, '//*[@id="x-auto-106"]').click()  # Click to expand Region menu
    driver.find_element(By.ID, 'x-auto-105-input').send_keys("Default")  # Region: select ID=x-auto-106
    driver.find_element(By.ID, 'gwt-debug-newLoginId-input').send_keys("t1-admin")  # Username
    driver.find_element(By.ID, 'gwt-debug-newPassword-input').send_keys("password")  # Password
    driver.find_element(By.ID, 'gwt-debug-newFirstName-input').send_keys("Tenant")  # First name
    driver.find_element(By.ID, 'gwt-debug-newLastName-input').send_keys("1")  # Last name
    driver.find_element(By.ID, 'gwt-debug-newEmail-input').send_keys("t1@brightpattern.com")  # Email

    driver.find_element(By.ID, 'gwt-debug-newMaxConcurrentUsers-input').send_keys("10")  # Max users
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # CLick to expand Database
    # server menu
    pyautogui.click(700, 835)

    driver.find_element(By.ID, 'gwt-debug-newDbName-input').send_keys("_db")  # Database name
    driver.find_element(By.ID, 'gwt-debug-newDbUser-input').send_keys("_db_usr")  # Username
    driver.find_element(By.ID, 'gwt-debug-newDbPassword-input').send_keys("password")  # Password
    driver.find_element(By.XPATH, "//button[text()='OK']").click()  # Click on OK


def test_set_status_active(init_driver):
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="x-auto-82"]').click()  # find Status menu expander
    pyautogui.click(940, 510)  # expand Status menu

    driver.find_element(By.XPATH, '//*[@id="gwt-debug-entity-update"]/tbody/tr[2]/td[2]/em/button').click()  # apply


def test_apply_pass_db(init_driver):
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-dbPassword-input"]').send_keys("password")  # send password
    driver.find_element(By.XPATH, '//*[@id="x-auto-136"]/tbody/tr[2]/td[2]/em/button').click()  # click Apply on DB


def test_ok_apply(init_driver):
    time.sleep(2)
    # driver.find_element(By.ID, 'x-auto-152').click()  # OK
    driver.find_element(By.XPATH, '//*[@id="x-auto-144"]/tbody/tr[2]/td[2]/em/button').send_keys(Keys.ESCAPE)  # OK
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-entity-update"]/tbody/tr[2]/td[2]/em/button').click()  # apply


"""
pytest test_sp_service_provider_add_tenant.py -v --capture=tee-sys --html=test_sp_service_provider_add_tenant.py.html

"""
