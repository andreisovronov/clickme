from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()  # или любой другой браузер, который вы предпочитаете
driver.get('http://www.example.com')  # измените на нужный URL

element = driver.find_element(By.ID, "myButton")  # замените "myButton" на идентификатор вашего элемента

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
