{
  
import allure
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Initialize logging
logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@allure.title("Validate error handling when destination is missing")
def test_missing_destination():
    # Set up Chrome driver
    service = Service("path/to/chromedriver")
    service.start()
    driver = webdriver.Remote(service.service_url)
    
    try:
        with allure.step("Open the site"):
            driver.get("URL")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            
        with allure.step("Leave the Destination field empty"):
            start_date = "01/01/2023"
            budget = "1000"
            interests = "Sightseeing"
            
            driver.find_element(By.ID, "start_date").send_keys(start_date)
            driver.find_element(By.ID, "budget").send_keys(budget)
            driver.find_element(By.ID, "interests").send_keys(interests)
            
        with allure.step("Click the 'Generate' button"):
            driver.find_element(By.ID, "generate_button").click()
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            
            error_message = driver.find_element(By.ID, "error_message").text
            assert "Please enter a destination" in error_message
            logging.info("Error message displayed: Please enter a destination")
        
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        logging.error(f"Test failed: {str(e)}")
        raise
        
    finally:
        driver.quit()
        service.stop()
        
if __name__ == "__main__":
    test_missing_destination()

}

