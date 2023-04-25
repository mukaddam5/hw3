from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\Admin\\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("http://shopping.beeyor.com/")
print(driver.current_url)
# (//a[@href='http://shopping.beeyor.com/shop/'])[1]
sleep(2)
driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1] ").click()
print(driver.current_url)
sleep(2)
driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[2]").click()
sleep(5)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[title= 'View your shopping cart']")).perform()
# Info for Relative XPATH:
# Relative XPATH syntax starts with //,
# follows with the tag name and @ sign, then attribute and value
# (//a[@href='http://shopping.beeyor.com/shop/'])[1]
sleep(5)

driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward wp-element-button").click()
sleep(5)
# CSS info below:
# Css locator syntax similar to XPATH,but no // and @
# a[class="button wc-forward wp-element-button"]

driver.close()


















