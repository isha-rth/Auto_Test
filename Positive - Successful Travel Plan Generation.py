{
  "text": "import logging
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure_pytest

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://aukrk.github.io/locai-frontend/")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "destination")))

# Find the input fields and buttons
destination_input = driver.find_element(By.ID, "destination")
date_input = driver.find_element(By.ID, "date")
budget_input = driver.find_element(By.ID, "budget")
currency_dropdown = driver.find_element(By.ID, "currency")
activity_dropdown = driver.find_element(By.ID, "activity")
submit_button = driver.find_element(By.ID, "generate")

# Enter the test data
destination_input.send_keys("Japan")
date_input.send_keys("05-09-2025")
budget_input.send_keys("5000")

# Select currency
currency_dropdown.send_keys("AUD")

# Select activity
activity_dropdown.send_keys("Museums")

# Submit the form
submit_button.click()

# Wait for the results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "results")))

# Take a screenshot on test failure
try:
    assert "Japan" in driver.title
except AssertionError:
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

# Capture the URL for reporting
url = driver.current_url
logging.info(f"Test completed. URL: {url}")

# Close the browser
driver.quit()"
}