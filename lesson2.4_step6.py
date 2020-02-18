from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    element = browser.find_element_by_id("button")
    #button.click()  
    #message = browser.find_element_by_id("verify_message")
    #assert "successful" in message.text
    #time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()
