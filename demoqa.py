from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")  # Replace with the actual URL  

sleep(10)
# Assume the XPath for the checkbox
checkbox_xpath = "//input[@id='hobbies-checkbox-3']"

# Locate the checkbox
checkbox = driver.find_element(By.XPATH, checkbox_xpath)

# Check if the checkbox is already selected
if not checkbox.is_selected():
    checkbox.click()
sleep(10)
# You can continue with other actions on the page or close the browser
driver.quit()
