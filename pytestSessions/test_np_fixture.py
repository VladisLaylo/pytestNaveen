from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("------------setup------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider')

    yield
    print("----------tear down----------")
    driver.quit()


def test_np_title(init_driver):
    assert driver.title == "Phone number provisioning"
    print("Title found: " + driver.title)


def test_np_urls(init_driver):
    assert driver.current_url == "https://vladis03.bugfocus.com/numberprovisioning/provider"
    print("URL found: " + driver.current_url)
