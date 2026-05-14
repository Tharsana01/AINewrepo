package com.agenticai;

import org.junit.jupiter.api.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {
    @Test
    void shouldNavigateToAngularPractice() {
        // If necessary, set the ChromeDriver executable path explicitly:
        // System.setProperty("webdriver.chrome.driver", "C:/path/to/chromedriver.exe");

        WebDriver driver = new ChromeDriver();
        try {
            String expectedUrl = "https://rahulshettyacademy.com/angularpractice/";
            driver.get(expectedUrl);
            assertEquals(expectedUrl, driver.getCurrentUrl());
        } finally {
            driver.quit();
        }
    }
}
