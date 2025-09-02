{
  "text": "Here is an example Selenium Python test script for the given test case:

```python
import logging
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
import allure

class ItineraryGenerationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()

    @allure.step("Navigate to the website")
    def test_navigate_to_website(self):
        self.driver.get("https://aukrk.github.io/locai-frontend/")
        self.assertTrue("Locai - Visit places you love" in self.driver.title)

    @allure.step("Generate Itinerary with valid data")
    def test_generate_itinerary(self):
        location = "Japan"
        date = "05-09-2025"
        budget = "5000"
        interest = "Museums"

        location_field = self.driver.find_element(By.ID, "location")
        date_field = self.driver.find_element(By.ID, "date")
        budget_field = self.driver.find_element(By.ID, "budget")
        interest_field = self.driver.find_element(By.ID, "interest")

        location_field.clear()
        location_field.send_keys(location)

        date_field.clear()
        date_field.send_keys(date)

        budget_field.clear()
        budget_field.send_keys(budget)

        interest_field.send_keys(interest)
        interest_field.send_keys(Keys.RETURN)

        generate_button = self.driver.find_element(By.ID, "generate-itinerary")
        generate_button.click()

        time.sleep(2)  # Adding a delay to wait for the itinerary to generate

        # Assertion to check if itinerary is displayed
        itinerary_section = self.driver.find_element(By.ID, "itinerary-section")
        self.assertTrue(itinerary_section.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

```

In this script:
- The `setUpClass` method sets up the WebDriver and opens the browser before the tests start.
- The `test_navigate_to_website` method navigates to the website and verifies the title.
- The `test_generate_itinerary` method enters the required data and generates the itinerary.
- Allure annotations are used for reporting.
- Screenshot on test failure and logging are not explicitly added in the script, but can be implemented as needed.

To run this script in IntelliJ, you can create a new Python test configuration and specify the path to this script. You will also need to install the `allure-pytest` package for Allure reporting and configure Allure accordingly.

Please adjust the script based on your project structure and requirements."
}