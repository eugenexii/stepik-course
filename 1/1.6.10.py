from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    labels = browser.find_elements(By.TAG_NAME,"label") # Список лэйблов над текстовыми полями
    inputs = browser.find_elements(By.TAG_NAME,"input") # Список текстовых полей

    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!"
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()