{

import logging
import unittest
import allure
from selenium import webdriver
from datetime import date
import os

class TestTravelRecommendations(unittest.TestCase):

    @allure.step("Navigate to the website and validate recommendations")
    def test_travel_recommendations(self):
        logging.basicConfig(level=logging.INFO)
        driver_path = "path/to/chromedriver"
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        driver.get("https://aukrk.github.io/locai-frontend/")

        logging.info("Entering destination")
        destination_input = driver.find_element_by_id("destination")
        destination_input.send_keys("Japan")

        logging.info("Entering travel date")
        travel_date_input = driver.find_element_by_id("date")
        travel_date_input.send_keys("05-09-2025")

        logging.info("Entering budget")
        budget_input = driver.find_element_by_id("budget")
        budget_input.send_keys("5000 AUD")

        logging.info("Entering interest")
        interest_input = driver.find_element_by_id("interest")
        interest_input.send_keys("Museums")

        logging.info("Submitting the form")
        submit_button = driver.find_element_by_id("submit-btn")
        submit_button.click()

        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)

        recommendations = driver.find_element_by_xpath("//div[@id='recommendations']")
        self.assertTrue(recommendations.is_displayed(), "Recommendations are not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

}

