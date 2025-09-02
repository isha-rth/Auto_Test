{
  "text": "import logging
import allure
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.feature("Budget Field Validation")
class TestBudgetField:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Verify that budget field rejects negative values")
    def test_negative_budget(self):
        self.driver.get("http://examplewebsite.com")

        destination_input = self.driver.find_element(By.ID, "destination")
        destination_input.send_keys("Japan")

        travel_date_input = self.driver.find_element(By.ID, "travel-date")
        travel_date_input.send_keys("05-09-2025")

        budget_input = self.driver.find_element(By.ID, "budget")
        budget_input.send_keys("-1000 AUD")

        interest_select = self.driver.find_element(By.ID, "interest")
        interest_select.send_keys("Museums")

        generate_itinerary_button = self.driver.find_element(By.ID, "generate-itinerary")
        generate_itinerary_button.click()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "error-message"), "Budget cannot be negative")
            )
            logging.info("Negative budget validation successful")
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="Negative_Budget_Validation_Failure", attachment_type=allure.attachment_type.PNG)
            logging.error("Negative budget validation failed - error message not displayed")
            pytest.fail("Negative budget validation failed - error message not displayed")


if __name__ == "__main__":
    pytest.main(args=[os.path.abspath(__file__), "--alluredir", os.path.join(os.path.dirname(__file__), "allure-results")])"
}