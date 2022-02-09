from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("------------setup------------")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()

    yield
    print("----------tear down----------")
    time.sleep(5)
    driver.quit()


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

    driver.find_element(By.XPATH, "//input[@id='gwt-debug-newUrl-input']").send_keys("t1.bugfocus.com")  # Access domain
    # domain
    driver.find_element(By.ID, 'gwt-debug-newSip-input').send_keys("sip1.ru")  # SIP domain


def test_default_language(init_driver):  # expand DEFAULT LANGUAGE menu to get the list of items
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[5]/div['
                                  '1]/div/img').click()
    drop_list = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
    for ele in drop_list:
        print(ele.text)
        if ele.text == 'English - United States':  # find item to click
            ele.click()
            break


def test_default_timezone(init_driver):  # expand DEFAULT TIMEZONE menu to get the list of items
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[6]/div['
                                  '1]/div/img').click()
    drop_list = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
    for ele in drop_list:
        print(ele.text)
        if ele.text == '+00:00 Etc/UTC':  # find item to click
            ele.click()
            break


def test_default_country(init_driver):  # expand DEFAULT COUNTRY menu to get the list of items
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[7]/div['
                                  '1]/div/img').click()
    drop_list = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
    for ele in drop_list:
        print(ele.text)
        if ele.text == 'Russia':  # find item to click
            ele.click()
            break


def test_region_menu(init_driver):  # expand REGION menu to get the list of items
    driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/form/div[8]/div['
                                  '1]/div/table/tbody/tr/td[1]/div/img').click()
    drop_item = driver.find_elements(By.CSS_SELECTOR, 'span.E1LUYKC-c-l')  # collect list of menu items then print
    for ele in drop_item:
        print(ele.text)
        if ele.text == 'Default':  # find item to click
            ele.click()
            break


def test_continue_form(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newLoginId-input').send_keys("t1-admin")  # Username
    driver.find_element(By.ID, 'gwt-debug-newPassword-input').send_keys("password")  # Password
    driver.find_element(By.ID, 'gwt-debug-newFirstName-input').send_keys("Tenant")  # First name
    driver.find_element(By.ID, 'gwt-debug-newLastName-input').send_keys("1")  # Last name
    driver.find_element(By.ID, 'gwt-debug-newEmail-input').send_keys("t1@brightpattern.com")  # Email
    driver.find_element(By.ID, 'gwt-debug-newMaxConcurrentUsers-input').send_keys("10")  # Max users


def test_database_server(init_driver):  # expand DATABASE SERVER menu to get the list of items
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()
    drop_item = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
    for ele in drop_item:
        print(ele.text)
        if ele.text == 'vladis01.bugfocus.com':  # find item to click
            ele.click()
            break


def test_complete_form(init_driver):
    driver.find_element(By.ID, 'gwt-debug-newDbName-input').clear()  # Clear Database name
    driver.find_element(By.ID, 'gwt-debug-newDbName-input').send_keys("t1_db")  # Database name
    driver.find_element(By.ID, 'gwt-debug-newDbUser-input').clear()  # Clear Username
    driver.find_element(By.ID, 'gwt-debug-newDbUser-input').send_keys("t1_db_usr")  # Username
    driver.find_element(By.ID, 'gwt-debug-newDbPassword-input').send_keys("password")  # Password
    driver.find_element(By.XPATH, "//button[text()='OK']").click()  # Click on OK button
    time.sleep(10)


def test_set_status_active(init_driver):
    driver.find_element(By.XPATH, '//*[@id="x-auto-82"]').click()
    drop_menu = driver.find_elements(By.CSS_SELECTOR, 'div.x-combo-list-item')  # collect list of menu items then print
    for ele in drop_menu:
        print(ele.text)
        if ele.text == 'Active':  # find item to click
            ele.click()
            break
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-entity-update"]/tbody/tr[2]/td[2]/em/button').click()  # apply


def test_apply_pass_db(init_driver):
    time.sleep(2)
    driver.find_element(By.ID, 'gwt-debug-dbPassword-input').send_keys("password")  # send password
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div['
                                  '2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/form/div[4]/div['
                                  '1]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/em/button').click()  # click
    # Apply to DB


def test_ok_apply(init_driver):
    time.sleep(2)
    # driver.find_element(By.ID, 'x-auto-152').click()  # OK
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()  # Escape modal window with OK button
    # driver.send_keys(Keys.ESCAPE)  # Escape modal window with OK button
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-entity-update"]/tbody/tr[2]/td[2]/em/button').click()  # apply


"""
pytest pytestSessions/test_sp_service_provider_add_tenant.py

pytest pytestSessions/test_sp_service_provider_add_tenant.py -v --capture=tee-sys --html=reports/test_sp_sp_add_tenant.html

"""

"""    
    driver.find_element(By.XPATH, '//*[@id="gwt-debug-newDatabaseServer-input"]').click()  # Click to expand Database
    time.sleep(2)
    # pyautogui.click(700, 835)  # server menu on MacOS
    pyautogui.click(1130, 890)  # server menu on Windows 10

    driver.find_element(By.XPATH, '//*[@id="x-auto-106"]').click()  # Click to expand Region menu
    driver.find_element(By.ID, 'x-auto-105-input').send_keys("Default")  # Region: select ID=x-auto-106

    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="x-auto-82"]').click()  # find Status menu expander
    # pyautogui.click(940, 510)  # expand Status menu on MacOS
    pyautogui.click(1100, 458)  # expand Status menu on Windows 10

    driver.find_element(By.XPATH, '//*[@id="gwt-debug-entity-update"]/tbody/tr[2]/td[2]/em/button').click()  # apply
"""