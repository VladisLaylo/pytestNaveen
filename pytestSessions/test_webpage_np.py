from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def setup_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider')


def teardown_module():
    driver.quit()


def test_np_title():
    assert driver.title == "Phone number provisioning"


def test_np_urls():
    assert driver.current_url == "https://vladis03.bugfocus.com/numberprovisioning/provider"
