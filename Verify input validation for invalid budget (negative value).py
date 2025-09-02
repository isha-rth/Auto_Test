{
  "text": "import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("url_of_the_website_here")

# Find elements
budget_input = driver.find_element(By.ID, "budget-input")
submit_button = driver.find_element(By.ID, "submit-button")

# Enter negative budget amount
budget_input.send_keys("-1000")

# Fill other fields with valid data
# Assuming other fields have IDs as well, fill them here

@allure.step("Submit the form")
def submit_form():
    submit_button.click()

try:
    # Submit the form
    submit_form()
    
    # Wait for error message to appear
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-message"))
    )
    
    # Check if error message is displayed
    assert error_message.text == "The budget must be a positive value"
    logging.info("Test Passed: Error message displayed for negative budget value")
    
except Exception as e:
    logging.error("Test Failed: Error message not displayed for negative budget value")
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

# Close the browser
driver.quit()"
}