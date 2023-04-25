
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("C:\\Users\\Admin\\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("http://shopping.beeyor.com/")
sleep(2)
# driver.minimize_window()
print(driver.current_url)
print(driver.title)
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys("eShapalaq loop wakey machine")
driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys(Keys.ENTER)
sleep(5)
# driver.refresh()
driver.back()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys(Keys.CONTROL + "A")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").clear()
# driver.forward()
 # driver.close()






















































