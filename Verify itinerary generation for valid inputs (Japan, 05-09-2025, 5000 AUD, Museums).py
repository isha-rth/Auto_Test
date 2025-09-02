{
  "text": "import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import io.github.bonigarcia.wdm.WebDriverManager;
import io.qameta.allure.Attachment;

public class ItineraryTest {

    private WebDriver driver;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @Test
    public void testItineraryGeneration() {
        driver.get("https://aukrk.github.io/locai-frontend/");

        Select destinationSelect = new Select(driver.findElement(By.id("destination")));
        destinationSelect.selectByVisibleText("Japan");

        WebElement travelDateInput = driver.findElement(By.id("travel-date"));
        travelDateInput.sendKeys("05-09-2025");

        WebElement budgetInput = driver.findElement(By.id("budget"));
        budgetInput.sendKeys("5000");

        Select interestSelect = new Select(driver.findElement(By.id("interest")));
        interestSelect.selectByVisibleText("Museums");

        driver.findElement(By.id("generate-btn")).click();

        // Add assertion to verify the generated itinerary here
    }

    @Attachment
    public byte[] takeScreenshot() {
        return ((org.openqa.selenium.TakesScreenshot) driver).getScreenshotAs(org.openqa.selenium.OutputType.BYTES);
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            takeScreenshot();
            driver.quit();
        }
    }
}"
}