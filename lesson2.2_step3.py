from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
#browser.find_element_by_tag_name("select").click()
#browser.find_element_by_css_selector("option:nth-child(2)").click()
#Последняя строчка может выглядеть и так:

#browser.find_element_by_css_selector("[value='1']").click()

#from selenium.webdriver.support.ui import Select
#select = Select(browser.find_element_by_tag_name("select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"

#Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый #способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего #примера.

#Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. Для того чтобы найти #элемент с текстом "Python", нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном примере #имеет значение по умолчанию равное "--".

try:
    browser = webdriver.Chrome()
    browser.get(link2)
    x_element = browser.find_element_by_id('num1')
    x = x_element.text
	#x1= int([x],10)
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    z = int(x) + int(y)
    str = str(z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
	
    
finally:
    time.sleep(10)
    browser.quit()
