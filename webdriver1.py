from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

sleep(10)
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Huynh")

driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Nhi")

driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("aaa@gmail.com")

driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("123456789")

driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").send_keys("20/11/2002")

a = driver.find_element(By.XPATH, "//div[@id='subjectsContainer']//following::input").send_keys("Maths")

driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-3']")

driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Quy Nhon")

sleep(10)
driver.close()


