from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    windows = browser.window_handles
    current_window = browser.current_window_handle
    for win in windows:
        if current_window == win:
            print(win, " with current index: ", windows.index(win))
        else:
            print(win, " with index: ", windows.index(win))
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()
