from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID, 'justAnotherInputBox').click()

time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 6':
        ele.click()
        break

time.sleep(2)
driver.quit()


"""
pytest pytestSessions/JqueryDropDownMenu.py -v --capture=tee-sys --html=reports/JqueryDropDownMenu.html

Lesson: https://youtu.be/bdU0Hqggwjw
"""