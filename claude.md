# AgenticAi Selenium Project

## Project Overview
This is a Java-based Selenium automation project designed for web testing and browser automation. The project demonstrates basic Selenium WebDriver usage with Chrome browser integration.

## Technologies Used
- **Java 17**: Programming language
- **Maven**: Build and dependency management tool
- **Selenium WebDriver 4.15.0**: Browser automation framework
- **JUnit 5.10.0**: Testing framework
- **ChromeDriver**: WebDriver implementation for Chrome browser

## Project Structure
```
src/
├── main/java/com/agenticai/
│   └── App.java              # Main application class
└── test/java/com/agenticai/
    └── AppTest.java          # Test class
pom.xml                       # Maven configuration
target/                       # Build output directory
```

## Main Components

### App.java
The main application class that demonstrates basic Selenium functionality:
- Initializes Chrome WebDriver
- Navigates to example.com
- Prints the page title
- Properly closes the browser

### AppTest.java
JUnit test class containing:
- Test method that navigates to Rahul Shetty Academy's Angular practice site
- URL assertion to verify navigation success

## Dependencies
- **selenium-java**: Core Selenium WebDriver functionality
- **junit-jupiter**: JUnit 5 testing framework (test scope)

## Build and Run Instructions

### Prerequisites
- Java 17 or higher installed
- Maven installed
- Chrome browser installed
- ChromeDriver (automatically managed by Selenium Manager in newer versions)

### Building the Project
```bash
mvn clean compile
```

### Running Tests
```bash
mvn test
```

### Running the Main Application
```bash
mvn exec:java -Dexec.mainClass="com.agenticai.App"
```

### Package the Application
```bash
mvn package
```

## Configuration Notes
- ChromeDriver path can be set explicitly if needed using `System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe")`
- The project uses Selenium Manager (introduced in Selenium 4.11+) which automatically manages WebDriver binaries

## Test Results
Test results are generated in `target/surefire-reports/` directory with detailed XML and text reports.