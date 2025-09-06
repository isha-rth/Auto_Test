{
  "text": "import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import io.qameta.allure.Allure;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

@Epic("Trip Planning")
@Feature("Successful Trip Plan Creation")

public class TripPlanCreationTest {

    private WebDriver driver;

    @BeforeEach
    public void setup() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    public void testSuccessfulTripPlanCreation() {
        driver.get("https://aukrk.github.io/locai-frontend/");

        WebElement destinationField = driver.findElement(By.id("destination"));
        destinationField.sendKeys("Japan");

        WebElement startDateField = driver.findElement(By.id("start-date"));
        startDateField.sendKeys("05-09-2025");

        WebElement budgetField = driver.findElement(By.id("budget"));
        budgetField.sendKeys("5000");

        WebElement currencyDropdown = driver.findElement(By.id("currency"));
        currencyDropdown.sendKeys("AUD");

        WebElement interestDropdown = driver.findElement(By.id("interest"));
        interestDropdown.sendKeys("Museums");

        WebElement planTripButton = driver.findElement(By.id("plan-trip-button"));
        planTripButton.click();

        // Assertion for the expected result
        WebElement tripPlanSuggestion = driver.findElement(By.id("trip-plan-suggestion"));
        String tripPlanText = tripPlanSuggestion.getText();
        assert tripPlanText.contains("Japan");
        assert tripPlanText.contains("Museums");
        assert tripPlanText.contains("5000 AUD");
        assert tripPlanText.contains("05-09-2025");

        // Logging
        Allure.addAttachment("Trip Plan Suggestion", "text/plain", tripPlanText);

        // Screenshot on failure
        if (!tripPlanText.contains("Japan") || !tripPlanText.contains("Museums") || !tripPlanText.contains("5000 AUD") || !tripPlanText.contains("05-09-2025")) {
            Allure.addAttachment("Screenshot", "image/png", ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES));
        }
    }
}"
}