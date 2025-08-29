{
  "text": "Here's the Selenium Python test script for the given test case:

```python
import allure
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os

class TestBudgetValidation(unittest.TestCase):

    @allure.step("Open the site")
    def open_site(self):
        self.driver = webdriver.Chrome()
        self.driver.get("URL_OF_YOUR_SITE")

    @allure.step("Enter all fields with valid data, except enter a non-numeric value in the Budget field")
    def enter_invalid_budget(self):
        name_field = self.driver.find_element(By.ID, "name_field_id")
        name_field.send_keys("John Doe")

        email_field = self.driver.find_element(By.ID, "email_field_id")
        email_field.send_keys("johndoe@example.com")

        budget_field = self.driver.find_element(By.ID, "budget_field_id")
        budget_field.send_keys("five thousand")

        generate_button = self.driver.find_element(By.ID, "generate_button_id")
        generate_button.click()

    @allure.step("Verify error message for non-numeric budget value")
    def verify_error_message(self):
        error_message = self.driver.find_element(By.ID, "error_message_id").text
        assert "Budget must be numeric" in error_message

    @allure.step("Capture screenshot")
    def capture_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Close the browser")
    def close_browser(self):
        self.driver.quit()

    @allure.description("Validate rejection of non-numeric value in budget input")
    def test_validate_budget_validation(self):
        with allure.step("Test scenario"):
            self.open_site()
            self.enter_invalid_budget()
            self.verify_error_message()

    def test_main(self):
        with allure.step("Execute test case"):
            allure.dynamic.title("Validate rejection of non-numeric value in budget input")
            allure.dynamic.description("This test case validates the rejection of a non-numeric value in the budget input field.")
            try:
                self.test_validate_budget_validation()
            except AssertionError as e:
                logging.error("Test case failed: " + str(e))
                self.capture_screenshot()

            self.close_browser()

if __name__ == "__main__":
    unittest.main()

```

Note: Replace the placeholders such as "URL_OF_YOUR_SITE", element IDs, and other necessary details with the actual values from your application. This script uses the unittest framework and Allure for reporting. Remember to set up Allure in your project for the reporting to work."
}
