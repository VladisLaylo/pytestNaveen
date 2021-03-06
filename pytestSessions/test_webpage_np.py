from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://vladis03.bugfocus.com/numberprovisioning/provider')


def teardown_module(module):
    driver.quit()


def test_np_title():
    assert driver.title == "Phone number provisioning"


def test_np_urls():
    assert driver.current_url == "https://vladis03.bugfocus.com/numberprovisioning/provider"


"""
Setup generate to HTML report:
1. pip install pytest-html
2. py.test test_webpage_np.py -v -s --html=np_test_report.html
* if you want to change css styles in project folder: assets/style.css
"""