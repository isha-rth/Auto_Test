{
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;

public class ValidateInvalidTravelDateTest {

    private WebDriver driver;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
    }

    @Test
    public void testInvalidTravelDateErrorHandling() {
        driver.get("https://your-travel-site.com");
        WebElement destinationInput = driver.findElement(By.id("destination"));
        destinationInput.sendKeys("Japan");

        WebElement startDateInput = driver.findElement(By.id("start-date"));
        startDateInput.sendKeys("11/01/2020"); // Past date

        WebElement budgetInput = driver.findElement(By.id("budget"));
        budgetInput.sendKeys("2000");

        WebElement interestsInput = driver.findElement(By.id("interests"));
        interestsInput.sendKeys("Sightseeing, Food");

        WebElement generateButton = driver.findElement(By.id("generate-button"));
        generateButton.click();

        WebElement errorElement = driver.findElement(By.id("error-message"));
        String errorMessage = errorElement.getText();
        Assert.assertTrue(errorMessage.contains("invalid date"), "Error message for invalid date not displayed");

        // Take screenshot on test failure
        if (!errorMessage.contains("invalid date")) {
            ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
        }
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}"
}

