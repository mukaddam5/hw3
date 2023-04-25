from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\Admin\\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[href='/windows']").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
sleep(2)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)
sleep(2)
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
sleep(2)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_window_handle)
sleep(3)
driver.quit()




















