from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input_element = browser.find_element(By.ID, 'answer')
    input_element.send_keys(y)

    checkbox_element = browser.find_element(By.CSS_SELECTOR, '.form-check-custom input.form-check-input')
    checkbox_element.click()

    radiobox_element = browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]')
    radiobox_element.click()


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