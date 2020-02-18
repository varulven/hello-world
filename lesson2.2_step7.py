from selenium import webdriver
import time 
import os 
from selenium.webdriver.support.ui import Select

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    #element.send_keys(file_path)
    time.sleep(5)
finally:
    time.sleep(10)
    #browser.quit()
