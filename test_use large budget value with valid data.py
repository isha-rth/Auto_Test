import time
import logging
import allure
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://aukrk.github.io/locai-frontend/")
logger.info("Website opened successfully")

# Test Case Title
test_case_title = "Use large budget value with valid data"

# Test Case Steps
with allure.step("Enter 'Japan' as destination"):
    destination_input = driver.find_element(By.ID, "destination")
    destination_input.clear()
    destination_input.send_keys("Japan")
    logger.info("Entered 'Japan' as destination")

with allure.step("Enter '05-09-2025' as date"):
    date_input = driver.find_element(By.ID, "date")
    date_input.clear()
    date_input.send_keys("05-09-2025")
    logger.info("Entered '05-09-2025' as date")

with allure.step("Enter '1000000 AUD' as budget"):
    budget_input = driver.find_element(By.ID, "budget")
    budget_input.clear()
    budget_input.send_keys("1000000 AUD")
    logger.info("Entered '1000000 AUD' as budget")

with allure.step("Select 'Museums' as the activity"):
    activity_select = Select(driver.find_element(By.ID, "activity"))
    activity_select.select_by_visible_text("Museums")
    logger.info("Selected 'Museums' as the activity")

with allure.step("Submit the form"):
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()
    logger.info("Form submitted successfully")

# Wait for the result to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "itinerary"))
)

# Check if the itinerary is generated
itinerary_element = driver.find_element(By.ID, "itinerary")
itinerary_text = itinerary_element.text

with allure.step("Verify the itinerary is generated with possibly more premium options"):
    assert "Premium" in itinerary_text, "Itinerary did not contain premium options"
    logger.info("Itinerary generated with possibly more premium options")

# Capture screenshot on test failure
if "Premium" not in itinerary_text:
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

# Close the browser
driver.quit()

# Allure reporting
allure.dynamic.title(test_case_title)
allure.dynamic.description_html(
    f'<h3><span style="color: green;">Test Case Steps:</span></h3>'
    f'<ol>'
    f'<li>Enter "Japan" as destination</li>'
    f'<li>Enter "05-09-2025" as date</li>'
    f'<li>Enter "1000000 AUD" as budget</li>'
    f'<li>Select "Museums" as the activity</li>'
    f'<li>Submit the form</li>'
    f'</ol>'
)
if "Premium" in itinerary_text:
    allure.dynamic.description_html('<h4><span style="color: green;">Expected Result: Itinerary is generated with possibly more premium options</span></h4>')
else:
    allure.dynamic.description_html('<h4><span style="color: red;">Expected Result: Itinerary is generated with possibly more premium options</span></h4>')

