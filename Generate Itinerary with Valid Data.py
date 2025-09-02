{
  "text": "import allure
import logging
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestGenerateItinerary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def tearDown(self):
        if self._outcome.errors:
            # On test failure, capture screenshot and save as file
            self.driver.save_screenshot(os.path.join(os.getcwd(), "screenshot.png"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.step("Enter Destination, Travel Date, Budget, Currency, Activity Preference and Generate Itinerary")
    def generate_itinerary(self):
        self.driver.get("http://website-url.com")  # Update with the actual website URL

        destination_field = self.driver.find_element(By.ID, "destination")
        destination_field.send_keys("Japan")

        travel_date = self.driver.find_element(By.ID, "travel-date")
        travel_date.send_keys("05-09-2025")

        budget_field = self.driver.find_element(By.ID, "budget")
        budget_field.send_keys("5000")

        currency_dropdown = Select(self.driver.find_element(By.ID, "currency"))
        currency_dropdown.select_by_visible_text("AUD")

        activity_preference = self.driver.find_element(
            By.XPATH, "//input[@type='radio' and @value='museums']")
        activity_preference.click()

        generate_itinerary_button = self.driver.find_element(By.ID, "generate-itinerary")
        generate_itinerary_button.click()

        time.sleep(5)  # Wait for itinerary generation

    @allure.description("Test to Generate Itinerary with Valid Data")
    def test_generate_itinerary_with_valid_data(self):
        logging.info("Starting test to generate itinerary with valid data")
        self.generate_itinerary()
        logging.info("Completed test to generate itinerary with valid data")

if __name__ == "__main__":
    unittest.main()"
}