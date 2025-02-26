from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answerInput = browser.find_element(By.ID, "answer")
    answerInput.send_keys(y)
    
    buttonCheckbox = browser.find_element(By.ID, "robotCheckbox")
    buttonCheckbox.click()
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    buttonRobots = browser.find_element(By.ID, "robotsRule")
    buttonRobots.click()
    
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()