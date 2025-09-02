{
  "text": "import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

public class UnsupportedDestinationTest {
    private WebDriver driver;

    @BeforeClass
    public void setup() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void testUnsupportedDestination() {
        driver.get("https://example.com");

        WebElement destinationInput = driver.findElement(By.id("destination"));
        destinationInput.sendKeys("Atlantis");

        WebElement dateInput = driver.findElement(By.id("date"));
        dateInput.sendKeys("10/25/2022");

        WebElement budgetInput = driver.findElement(By.id("budget"));
        budgetInput.sendKeys("1000");

        WebElement interestInput = driver.findElement(By.id("interest"));
        interestInput.sendKeys("Beach");

        WebElement generateButton = driver.findElement(By.id("generate-button"));
        generateButton.click();

        WebElement errorMessage = driver.findElement(By.id("error-message"));
        String errorText = errorMessage.getText();
        Assert.assertTrue(errorText.contains("unsupported destination") || errorText.contains("no itinerary is generated"));
    }

    @AfterClass
    public void teardown() {
        if (driver != null) {
            driver.quit();
        }
    }
}"
}