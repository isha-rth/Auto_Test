import allure
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@allure.step("Enter unrealistically low budget test")
def test_enter_low_budget():
    logging.basicConfig(level=logging.INFO)

    logging.info("Setting up driver")
    driver = webdriver.Chrome()

    allure.dynamic.title("Enter Unrealistically Low Budget Test")
    allure.dynamic.description("Test case to enter a low budget and check system response")

    try:
        logging.info("Navigating to the test site")
        driver.get("http://example.com")

        logging.info("Entering destination")
        destination_input = driver.find_element(By.ID, "destination")
        destination_input.send_keys("Japan")

        logging.info("Entering date")
        date_input = driver.find_element(By.ID, "date")
        date_input.send_keys("05-09-2025")

        logging.info("Entering low budget")
        budget_input = driver.find_element(By.ID, "budget")
        budget_input.send_keys("1 AUD")

        logging.info("Selecting activity")
        activity_select = driver.find_element(By.ID, "activity")
        activity_select.send_keys("Museums")
        
        logging.info("Submitting form")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Capture screenshot on test failure
        if "No viable options" not in driver.page_source:
            logging.error("System did not warn user about low budget but processed input")
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        logging.exception("An exception occurred: {}".format(str(e)))
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

    finally:
        logging.info("Closing the browser")
        driver.quit()

if __name__ == "__main__":
    test_enter_low_budget()
