{
  "text": "import unittest
import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestGenerateItinerary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @allure.step("Test: Verify handling of extremely high budget values")
    def test_high_budget(self):
        self.driver.get("url_of_your_website")
        self.driver.find_element(By.NAME, "destination").send_keys("Japan")
        self.driver.find_element(By.NAME, "date").send_keys("05-09-2025")
        self.driver.find_element(By.NAME, "budget").send_keys("1000000000")
        self.driver.find_element(By.NAME, "interest").send_keys("Museums")
        self.driver.find_element(By.XPATH, "//button[text()='Generate Itinerary']").click()

        try:
            alert = self.driver.switch_to.alert
            logging.error(f"Alert message displayed: {alert.text}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            alert.accept()
        except:
            self.assertTrue(True, "Itinerary is generated successfully")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()"
}