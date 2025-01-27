from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    
    # Переводим полученные значения из string формата в integer 
    num1_int = int(num1)
    num2_int = int(num2)
    
    # Складываем два числа
    res = num1_int + num2_int

    # Переводим значения из integer формата в string
    res_str = str(res)
    
    # Делаем выбор из selecta
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res_str)

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()