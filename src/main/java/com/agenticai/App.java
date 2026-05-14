package com.agenticai;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class App {
    public static void main(String[] args) {
        System.out.println("Starting Selenium WebDriver...");

        // If necessary, set the ChromeDriver executable path explicitly:
        // System.setProperty("webdriver.chrome.driver", "C:/path/to/chromedriver.exe");

        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://example.com");
            System.out.println("Page title: " + driver.getTitle());
        } finally {
            driver.quit();
        }
    }
}
