from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_xpath_form"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Evgenii")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Vygovskii")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("St-Petersburg")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    button = browser.find_element("xpath", "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

