from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
import time

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
elif browserName == "edge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browserName == "IE":
    driver = webdriver.Ie(IEDriverManager().install())
else:
    print("Please pass the correct browser name in WebDriverManager_CrossBrowser.py file: " + browserName)
    raise Exception('driver is not found in WebDriverManager_CrossBrowser.py')

driver.implicitly_wait(10)
driver.get("https://vladis03.bugfocus.com/numberprovisioning/provider")
driver.find_element(By.ID, 'username').send_keys("admin")
driver.find_element(By.ID, 'password').send_keys("password")
driver.find_element(By.XPATH, '//*[@id="appContainer"]/div/div/div/div[2]/form/div/div[3]/div/button').click()

print(driver.title)

time.sleep(2)
driver.quit()

"""
How to setup cross-browser selenium driver:
1. Google search: webdriver manager python
2. https://pypi.org/project/webdriver-manager/
3. PyCharm Terminal > pip install webdriver-manager
4. from webdriver_manager.chrome import ChromeDriverManager (top file code)
"""