{
  "text": "```python
import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("URL_TO_YOUR_APPLICATION")

# Define the test function
@allure.title("Attempt to submit with missing activity type")
@allure.description("Enter required details and try to submit without selecting an activity")
def test_missing_activity():
    try:
        logging.info("Entering destination")
        destination_input = driver.find_element(By.ID, "destination")
        destination_input.send_keys("Japan")

        logging.info("Entering date")
        date_input = driver.find_element(By.ID, "date")
        date_input.send_keys("05-09-2025")

        logging.info("Entering budget")
        budget_input = driver.find_element(By.ID, "budget")
        budget_input.send_keys("5000 AUD")

        # Do not select any activity

        logging.info("Clicking submit")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Wait for error message to appear
        time.sleep(1)
        
        # Check if error message is displayed
        error_message = driver.find_element(By.ID, "error_message").text
        assert "Please select an activity" in error_message
        logging.info("Error message displayed successfully")

    except Exception as e:
        # Capture screenshot on test failure
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        logging.error(f"An error occurred: {str(e)}")

# Run the test
test_missing_activity()

# Quit the webdriver
driver.quit()
```

Make sure to replace `"URL_TO_YOUR_APPLICATION"` with the actual URL of your application. Also, ensure that the element IDs used in the script (`"destination"`, `"date"`, `"budget"`, `"submit"`, `"error_message"`) match the IDs of the corresponding elements on your webpage."
}