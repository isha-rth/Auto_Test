import time
import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://aukrk.github.io/locai-frontend/")
logging.info("Opened the website")

# Fill in the form
destination_field = driver.find_element(By.ID, "locationInput")
destination_field.send_keys("Japan")

start_date_field = driver.find_element(By.ID, "dateInput")
start_date_field.send_keys("05-09-2025")

budget_field = driver.find_element(By.ID, "budgetInput")
budget_field.send_keys("5000")

interests_dropdown = driver.find_element(By.ID, "interestsInput")
interests_dropdown.send_keys("Museums")

# Click on Generate button
generate_button = driver.find_element(By.ID, "generate")
generate_button.click()
time.sleep(5)  # Wait for itinerary to generate

# Assertion for verifying the itinerary
itinerary_displayed = driver.find_element(By.ID, "itinerary")
assert "Japan" in itinerary_displayed.text, "Unexpected itinerary generated"
logging.info("Itinerary generated successfully")

# Capture screenshot on test failure
try:
    assert "Japan" in itinerary_displayed.text
except AssertionError:
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    logging.error("Test failed. Screenshot captured.")

# Close the browser
driver.quit()

