{
  "text": "import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import logging
import os

class TestBudgetFieldValidation(unittest.TestCase):

    @allure.step("Setting up the test")
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.step("Verify currency format enforcement in budget field")
    def test_verify_budget_field(self):
        logging.basicConfig(filename="test.log", level=logging.INFO)
        self.driver.get("url_of_your_web_application")

        destination_field = self.driver.find_element(By.ID, "destination")
        destination_field.send_keys("Japan")

        travel_date_field = self.driver.find_element(By.ID, "travel_date")
        travel_date_field.send_keys("05-09-2025")

        budget_field = self.driver.find_element(By.ID, "budget")
        budget_field.send_keys("5000")

        interest_field = self.driver.find_element(By.ID, "interest")
        interest_field.send_keys("Museums")

        generate_button = self.driver.find_element(By.ID, "generate_button")
        generate_button.click()

        try:
            self.driver.find_element(By.ID, "success_message")
            logging.info("Itinerary successfully generated.")
        except Exception as e:
            logging.error("Failed to generate itinerary. Please check budget field format.")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            self.fail("Failed to generate itinerary.")

    @allure.step("Tearing down the test")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()"
}