from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    #button = WebDriverWait(browser, 5).until_not(
        #EC.element_to_be_clickable((By.ID, "verify"))
    #)
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    
finally:
    time.sleep(10)
    browser.quit()
