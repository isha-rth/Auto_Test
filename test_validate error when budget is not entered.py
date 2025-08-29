 import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@allure.feature("Budget Based Itinerary Generator")
@allure.title("Validate error when budget is not entered")
def test_validate_error_when_budget_not_entered():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the site
        driver.get("https://example.com")

        # Enter all required fields except Budget
        driver.find_element(By.ID, "field1").send_keys("Value1")
        driver.find_element(By.ID, "field2").send_keys("Value2")

        # Click the 'Generate' button
        driver.find_element(By.ID, "generateButton").click()

        # Verify error message
        error_message = driver.find_element(By.ID, "errorMessage").text
        assert "Please enter a budget." in error_message

        # Capture screenshot on test failure
        if "Please enter a budget." not in error_message:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            logger.error("Error message not displayed.")

        logger.info("Test case passed. Error message displayed correctly.")

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        logger.error("Exception occurred: " + str(e))
        assert False

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_validate_error_when_budget_not_entered()
