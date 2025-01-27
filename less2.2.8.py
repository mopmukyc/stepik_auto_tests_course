from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Firstname')
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Lastname')
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('Email')
      
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'document.txt')       # добавляем к этому пути имя файла 

    file_el = browser.find_element(By.XPATH, '//input[@type="file"]')
    file_el.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()