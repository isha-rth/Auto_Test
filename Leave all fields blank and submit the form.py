{
  "text": "import unittest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure

class FormTest(unittest.TestCase):

    @allure.feature("Form Submission")
    @allure.title("Leave all fields blank and submit form")
    def test_leave_blank_fields(self):
        logging.basicConfig(level=logging.INFO)
        self.driver = webdriver.Chrome()
        self.driver.get("http://yourwebsite.com/form")

        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        time.sleep(2)  # Wait for validation errors to display

        error_messages = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'error-message')]")
        
        with allure.step("Verify validation errors"):
            for error_message in error_messages:
                assert "This field is required" in error_message.text

        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()"
}