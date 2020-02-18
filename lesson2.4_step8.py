from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/wait2.html"
link2 = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link2)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        # text_to_be_present_in_element_value((By.ID, "price", "100"))
    )
    # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
    # button = WebDriverWait(browser, 5).until_not(
    # EC.element_to_be_clickable((By.ID, "verify"))
    # )
    button = browser.find_element_by_id("book")
    button.click()
    # message = browser.find_element_by_id("verify_message")
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    button1 = browser.find_element_by_id("solve")
    button1.click()
    # assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()