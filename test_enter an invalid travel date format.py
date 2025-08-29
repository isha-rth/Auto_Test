{
import logging
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://exampletravelwebsite.com')

# Main test logic
def test_invalid_date_format():
    destination = 'Japan'
    date = '9th May 2025'
    budget = '5000 AUD'
    activity = 'Museums'
    
    # Enter destination
    destination_input = driver.find_element(By.ID, "destination")
    destination_input.send_keys(destination)
    
    # Enter invalid date
    date_input = driver.find_element(By.ID, "date")
    date_input.send_keys(date)
    
    # Enter budget
    budget_input = driver.find_element(By.ID, "budget")
    budget_input.send_keys(budget)
    
    # Select activity
    activity_dropdown = driver.find_element(By.ID, "activity")
    activity_dropdown.select_by_visible_text(activity)
    
    # Click submit
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    # Verify error message for date format
    error_message = driver.find_element(By.ID, "error_message").text
    assert error_message == "Please enter a valid date format (DD/MM/YYYY)"
    

# Execute the test
if __name__ == "__main__":
    try:
        test_invalid_date_format()
        logging.info("Test passed.")
    except Exception as e:
        logging.error("Test failed. Error: {}".format(str(e)))
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    finally:
        allure.dynamic.title("Enter an invalid travel date format")
        driver.quit()

}


