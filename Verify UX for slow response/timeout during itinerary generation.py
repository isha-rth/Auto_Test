{
  "text": "import allure
import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.testcase("Verify UX for slow response/timeout during itinerary generation")
def test_slow_response_itinerary_generation(driver):
    logging.info("Initiating itinerary generation with valid data...")
    driver.get("https://example.com")
    
    country_input = driver.find_element(By.ID, "country")
    country_input.send_keys("Japan")
    
    date_input = driver.find_element(By.ID, "date")
    date_input.send_keys("05-09-2025")
    
    budget_input = driver.find_element(By.ID, "budget")
    budget_input.send_keys("5000 AUD")
    
    activity_input = driver.find_element(By.ID, "activity")
    activity_input.send_keys("Museums")
    
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    logging.info("Simulating slow network or server delay...")
    time.sleep(30)  # Simulating 30 seconds delay
    loading_indicator = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loading-indicator")))
    
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "success-message")))
        logging.info("Itinerary generation successful!")
    except:
        logging.error("Itinerary generation failed or timed out.")
        allure.attach(driver.get_screenshot_as_png(), name="Itinerary_Generation_Failure", attachment_type=AttachmentType.PNG)
        assert False, "Itinerary generation failed or timed out"

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=reports"])"
}