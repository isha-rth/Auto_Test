{
import allure
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSubmitForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @allure.step("Fill out form and submit with missing destination")
    def test_missing_destination_error(self):
        self.driver.get("URL_OF_YOUR_FORM")

        date_input = self.driver.find_element(By.ID, "date")
        budget_input = self.driver.find_element(By.ID, "budget")
        activity_dropdown = self.driver.find_element(By.ID, "activity")
        submit_button = self.driver.find_element(By.ID, "submit")

        date_input.send_keys("05-09-2025")
        budget_input.send_keys("5000 AUD")
        activity_dropdown.send_keys("Museums")
        submit_button.click()

        error_message = self.driver.find_element(By.CLASS_NAME, "error-message").text
        assert "Please enter a destination" in error_message

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


# Logging configuration
logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Adding screenshot capture on test failure
def run(self):
    try:
        super().run(self)
    except Exception:
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise

# Allure report integration
!pip install pytest-allure-adaptor
!pip install allure-pytest

# In IntelliJ, run the test with the following command:
# pytest --alluredir=results TestSubmitForm.py

# After running the test, generate the report by executing:
# allure serve results"
}

