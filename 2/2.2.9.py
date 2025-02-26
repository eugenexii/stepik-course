from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '2.2.9.txt')  
print(str(file_path))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполнение поля "Имя"
    nameInput = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    nameInput.send_keys("Name")

    # Заполнение поля "Фамилия"
    lastnameInput = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastnameInput.send_keys("Surname")

    # Заполнение поля "Email"
    emailInput = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    emailInput.send_keys("pochta@mail.com")
    
    fileButton = browser.find_element(By.CSS_SELECTOR,"[type='file']")
    fileButton.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()