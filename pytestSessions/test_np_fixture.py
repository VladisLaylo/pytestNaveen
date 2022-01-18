from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    # print("------------setup------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider')

    yield
    # print("----------tear down----------")
    time.sleep(2)
    driver.quit()


def test_np_title(init_driver):
    assert driver.title == "Phone number provisioning"
    print("Title found: " + driver.title)


def test_np_urls(init_driver):
    assert driver.current_url == "https://vladis03.bugfocus.com/numberprovisioning/provider"
    print("URL found: " + driver.current_url)


def test_login():
    driver.find_element(By.ID, 'username').send_keys("admin")
    driver.find_element(By.ID, 'password').send_keys("password")
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()
    print("You are logged in")


def test_click_on_ph():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[1]/div/a[2]').click()
    print("You are on Orders page")


def test_expand_tenants_menu_in_orders():  # didn't find options_list
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[4]/div/div/div[2]/div/i').click()
    options_list = driver.find_elements(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[4]/div/div/div['
                                                  '2]/div/div[2]')  # find all prediction keywords

    for ele in options_list:  # print all prediction keywords
        print(ele.text)
        if ele.text == "a3Tenant61.com":  # click on this keyword
            ele.click()
            break  # break the loop
    print("You did expand the menu and tenant a3Tenant61 selected")


"""
pip install fixture
"""
