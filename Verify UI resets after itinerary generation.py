{
  "text": "import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;
import io.qameta.allure.Attachment;
import io.qameta.allure.Description;
import io.qameta.allure.Step;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class ItineraryGenerationTest {

    private WebDriver driver;
    private static final Logger logger = LogManager.getLogger(ItineraryGenerationTest.class);

    @BeforeClass
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @AfterClass
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @Description("Verify UI resets after itinerary generation")
    public void verifyUIResetAfterItineraryGeneration() {
        logger.info("Starting test case: Verify UI resets after itinerary generation");
        driver.get("http://www.example.com"); // Replace with the URL of the website
        generateItineraryWithValidData();
        clickResetButton();
        assertFieldsCleared();
        logger.info("Test case completed: Verify UI resets after itinerary generation");
    }

    @Step("Generate an itinerary with valid data")
    private void generateItineraryWithValidData() {
        // Implement logic to generate itinerary with valid data
        logger.info("Generating itinerary with valid data");
    }

    @Step("Click the reset/clear button")
    private void clickResetButton() {
        WebElement resetButton = driver.findElement(By.id("resetButton")); // Replace with the actual ID of the reset button
        resetButton.click();
        logger.info("Clicked the reset/clear button");
        captureScreenshot("reset_button_click");
    }

    @Step("Assert that all fields are cleared")
    private void assertFieldsCleared() {
        // Implement logic to check if input fields are cleared and previous results are hidden
        logger.info("Asserting that all fields are cleared and previous results are hidden");
        captureScreenshot("fields_cleared");
    }

    @Attachment(value = "{0}", type = "image/png")
    public byte[] captureScreenshot(String name) {
        return ((org.openqa.selenium.TakesScreenshot) driver).getScreenshotAs(org.openqa.selenium.OutputType.BYTES);
    }
}

Make sure to update the URL, element locators, and logic as per your application. This script will execute the test case and capture screenshots in case of failure. The Allure reporting integration will provide detailed reports for each test execution."
}