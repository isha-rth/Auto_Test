{
  "text": "import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import io.qameta.allure.Allure;
import io.qameta.allure.Step;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class TravelPlanTest {

    private WebDriver driver;

    @BeforeClass
    public void setup() {
        // Set the path to the ChromeDriver executable
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver.exe");

        // Configure Chrome options
        ChromeOptions options = new ChromeOptions();

        // Initialize Chrome driver
        driver = new ChromeDriver(options);

        // Maximize the browser window
        driver.manage().window().maximize();

        // Set the default waiting time
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    }

    @Test
    public void createTravelPlanTest() {
        openTravelPlanPage();
        fillTravelPlanForm("Japan", "05-09-2025", "5000", "AUD", "Museums");
        submitTravelPlanForm();
    }

    @Step("Open the travel plan page")
    private void openTravelPlanPage() {
        driver.get("https://aukrk.github.io/locai-frontend/");
    }

    @Step("Fill the travel plan form")
    private void fillTravelPlanForm(String destination, String date, String budget, String currency, String interest) {
        WebElement destinationField = driver.findElement(By.id("destination"));
        destinationField.sendKeys(destination);

        WebElement dateField = driver.findElement(By.id("date"));
        dateField.sendKeys(date);

        WebElement budgetField = driver.findElement(By.id("budget"));
        budgetField.sendKeys(budget);

        // Assuming the currency selection is a dropdown, you can implement the selection logic

        // Assuming the interest selection is a dropdown, you can implement the selection logic
    }

    @Step("Submit the travel plan form")
    private void submitTravelPlanForm() {
        WebElement generateButton = driver.findElement(By.id("generate-button"));
        generateButton.click();
    }

    @AfterClass
    public void tearDown() {
        captureScreenshotOnFailure();
        driver.quit();
    }

    private void captureScreenshotOnFailure() {
        File screenshot = ((ChromeDriver) driver).getScreenshotAs(OutputType.FILE);
        try {
            FileUtils.copyFile(screenshot, new File("screenshots/test_failure.png"));
            Allure.addAttachment("Screenshot on Failure", FileUtils.openInputStream(new File("screenshots/test_failure.png")));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}"
}