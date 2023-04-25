from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\Admin\\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://the-internet.herokuapp.com")
sleep(2)
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
sleep(5)
alert = driver.switch_to.alert
alert.accept()
text_for_first_alert = driver.find_element(By.CSS_SELECTOR, "#result")
print(text_for_first_alert.text)

sleep(4)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
sleep(3)
alert.dismiss()
text_for_second_alert = driver.find_element(By. ID, "result")
print(text_for_second_alert.text)
sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
sleep(2)
alert.send_keys("I am the best automation engineer")
sleep(5)
alert.accept()
text_for_third_alert = driver.find_element(By.ID, "result")
print(text_for_third_alert.text)













