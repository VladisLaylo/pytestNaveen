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


def test_bp_copyright(init_driver):
    bp_copyright = driver.find_element(By.CLASS_NAME, '_1WJJJRCXMXVPbjuQ4cAKzA')
    if bp_copyright.text == "Powered by Bright Pattern":
        print("Bright Pattern Copyright found: " + bp_copyright.text)
    else:
        print("Bright Pattern Copyright was not found")


def test_np_urls(init_driver):
    assert driver.current_url == "https://vladis03.bugfocus.com/numberprovisioning/provider"
    print("URL found: " + driver.current_url)


def test_login_into_np():
    driver.find_element(By.ID, 'username').send_keys("admin")
    driver.find_element(By.ID, 'password').send_keys("password")
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()
    print("You are logged in")


def test_open_orders_page():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[1]/div/a[2]').click()
    print("You are on Orders page before tenant selected")


def test_expand_tenants_menu_on_orders_page():  # didn't find options_list
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[4]/div/div/div[2]/div/i').click()
    print("Tenant menu expanded and collapsed")


def test_select_tenant_on_orders_page():
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='a3Tenant61.com']").click()
    print("Tenant named: a3Tenant61.com selected")


def test_open_order_details_page():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[4]/div[3]/div/div[1]/span').click()
    print("First order details page opened")


def test_return_to_orders_page():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[1]/i').click()
    print("Returned to Orders page")


def test_np_logout():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div[2]/div[1]/div[1]/div[2]/button').click()
    print("Logged out")


"""
pytest test_np_fixture.py -v --capture=tee-sys --html=np_test_fixture_report.html

pip install fixture

# to find prediction keyword check lesson https://www.youtube.com/watch?v=86nEglbjvIk
google: Naveen Automationlabs
ul.erkvQe li span

//span[text()='a3Tenant61.com']

"""

"""def test_np_title(init_driver):
    assert driver.title == "Phone number provisioning"
    print("Title found: " + driver.title)"""
