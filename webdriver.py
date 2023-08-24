from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(5)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
sleep(5)
driver.close()