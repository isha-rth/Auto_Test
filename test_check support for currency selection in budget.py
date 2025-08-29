{
import unittest
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import allure

class TestBudgetCurrencySelection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @allure.step("Open the site and enter details")
    def test_budget_currency_selection(self):
        self.driver.get("https://example.com")

        destination_input = self.driver.find_element(By.ID, "destination")
        destination_input.send_keys("Japan")

        date_input = self.driver.find_element(By.ID, "date")
        date_input.send_keys("05-09-2025")

        budget_input = self.driver.find_element(By.ID, "budget")
        budget_input.send_keys("5000")

        currency_dropdown = self.driver.find_element(By.ID, "currency")
        currency_dropdown.send_keys("AUD")

        interest_checkbox = self.driver.find_element(By.ID, "interest_museums")
        interest_checkbox.click()

        generate_button = self.driver.find_element(By.ID, "generate_button")
        generate_button.click()

        # Wait for the itinerary to be generated
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "itinerary")))

        # Capture screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        # Verify the generated itinerary
        assert "Japan" in self.driver.page_source
        assert "05-09-2025" in self.driver.page_source
        assert "AUD" in self.driver.page_source
        assert "5000" in self.driver.page_source
        assert "Museums" in self.driver.page_source

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



}



