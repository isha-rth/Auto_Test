import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
import allure

class TestInterestSelection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @allure.step('Open the site and test interest selection')
    def test_interest_selection_required(self):
        self.driver.get("url_of_the_site")

        destination = "Paris"
        date = "2022-12-25"
        budget = "1000"

        self.driver.find_element(By.ID, "destination").send_keys(destination)
        self.driver.find_element(By.ID, "date").send_keys(date)
        self.driver.find_element(By.ID, "budget").send_keys(budget)

        # Leave Interests empty
        self.driver.find_element(By.ID, "generate").click()

        with allure.step('Verify error message'):
            assert "Please select/enter at least one interest" in self.driver.page_source

    @allure.step("Take screenshot on test failure")
    def test_failed(self, exc):
        if exc is not None:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
