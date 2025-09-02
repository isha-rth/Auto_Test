{
  "text": "Here is a sample Selenium Python test script that covers the provided test case:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

class JapanRecommendationsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @allure.step("Navigate to the website")
    def test_navigate_to_website(self):
        self.driver.get("https://aukrk.github.io/locai-frontend/")
        self.assertEqual("Locai - Plan your trip", self.driver.title)

    @allure.step("Fill the form and generate recommendations")
    def test_generate_recommendations(self):
        self.driver.find_element(By.NAME, "destination").send_keys("Japan")
        self.driver.find_element(By.NAME, "date").send_keys("05-09-2025")
        self.driver.find_element(By.NAME, "budget").send_keys("5000")
        self.driver.find_element(By.NAME, "currency").send_keys("AUD")
        self.driver.find_element(By.NAME, "interest").send_keys("Museums")
        self.driver.find_element(By.XPATH, "/html/body/form/button").click()

        self.assertTrue(self.driver.find_element(By.ID, "recommendations").is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

To run this script in IntelliJ, you need to have the Selenium and Allure plugins installed. You can then create a new Python test in IntelliJ and copy-paste the code provided above.

Before running the script, make sure to install the necessary Python packages using pip:
```bash
pip install selenium allure-pytest
```

To capture screenshots on test failures, you can add a try-except block in the `tearDown` method to capture a screenshot when an assertion fails.

To integrate with Allure for reporting, you also need to add the necessary Allure annotations and configurations to your test script.

Note: This script assumes that you have the Chrome WebDriver installed and configured in your system path."
}