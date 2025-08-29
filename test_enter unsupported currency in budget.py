import time
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BudgetTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_enter_unsupported_currency(self):
        self.driver.get("URL_OF_TEST_APPLICATION")

        destination = self.driver.find_element(By.ID, "destination")
        destination.send_keys("Japan")

        date = self.driver.find_element(By.ID, "date")
        date.send_keys("05-09-2025")

        budget = self.driver.find_element(By.ID, "budget")
        budget.send_keys("5000 XYZ")

        activity = Select(self.driver.find_element(By.ID, "activity"))
        activity.select_by_visible_text("Museums")

        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

        error_message = self.driver.find_element(By.CLASS_NAME, "error-message").text
        assert "Unsupported currency" in error_message

        logging.info("Error message displayed: Unsupported currency")

        time.sleep(2)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
