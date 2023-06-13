import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import math
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("http://suninjuly.github.io/get_attribute.html")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_element = driver.find_element("css selector", "#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

driver.find_element("id", "answer").send_keys(y)
driver.find_element("id", "robotCheckbox").click()
driver.find_element("id", "robotsRule").click()
driver.find_element("class name", "btn.btn-default").click()
time.sleep(10)
