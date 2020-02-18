from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/wait1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_id("verify")
    button.click()  
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()
