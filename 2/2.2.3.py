from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text
    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text
    sum = int(a) + int(b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()