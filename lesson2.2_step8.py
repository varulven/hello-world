from selenium import webdriver
import time 
import os 
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Yana")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Myatezhnaya")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("vanapagan@list.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    
finally:
    time.sleep(10)
    browser.quit()
