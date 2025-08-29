{

import logging
import os
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Creating a function to capture screenshot on test failure
def take_screenshot(driver, file_path):
    driver.save_screenshot(file_path)
    allure.attach.file(file_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

# Initializing the WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Test Steps
with allure.step("Open the travel form"):
    driver.get("http://www.example.com/travel-form")

with allure.step("Enter destination as 'Japan'"):
    destination = driver.find_element(By.NAME, "destination")
    destination.send_keys("Japan")

with allure.step("Enter past date '05-09-2020' as travel date"):
    travel_date = driver.find_element(By.NAME, "travel_date")
    travel_date.send_keys("05-09-2020")

with allure.step("Enter '5000 AUD' as budget"):
    budget = driver.find_element(By.NAME, "budget")
    budget.send_keys("5000 AUD")

with allure.step("Select 'Museums' as preferred activity"):
    activity = Select(driver.find_element(By.NAME, "activity"))
    activity.select_by_visible_text("Museums")

with allure.step("Submit the form"):
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

# Check for error message
error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message")))
with allure.step("Verify error message"):
    assert error_message.text == "Travel date must be in the future"

# Taking screenshot on test failure
try:
    assert error_message.text == "Travel date must be in the future"
except AssertionError:
    file_path = os.path.join(os.getcwd(), "screenshot.png")
    take_screenshot(driver, file_path)
    logging.error("Test failed. Screenshot captured.")

# Closing the WebDriver
driver.quit()


}

