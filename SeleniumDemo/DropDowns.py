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
driver.get("http://shopping.beeyor.com/")
print(driver.current_url)
# (//a[@href='http://shopping.beeyor.com/shop/'])[1]
sleep(2)
driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1] ").click()
sleep(3)
select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
sleep(3)
# select.select_by_index(2)
# select.select_by_value("date")
list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    item.click()
sleep(3)
driver.find_element(By.XPATH, "(//a[@title='View cart'])[1]").click()
sleep(3)
driver.find_element(By.ID, "coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[name='apply_coupon']").click()
sleep(6)
actual_message = driver.find_element(By.CSS_SELECTOR, ".woocommerce-message").text
# expected_message = "Coupon code applied successfully."

assert "Coupon" in actual_message

# assert actual_message == expected_message
print(actual_message)
# print(expected_message)



















