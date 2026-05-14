# Test Scenarios Documentation - AgenticAi Selenium Project

## Overview
This document defines comprehensive test scenarios for the AgenticAi Selenium automation project. These scenarios cover basic browser automation, Angular form interactions, data validation, error handling, and end-to-end workflows.

---

## Test Scenario Category 1: Basic Browser Navigation

### TS-001: Navigate to Example.com
**Objective**: Verify browser can successfully navigate to example.com and retrieve page title

**Preconditions**:
- Chrome browser installed
- ChromeDriver available
- Internet connectivity established

**Test Steps**:
1. Initialize ChromeDriver
2. Navigate to https://example.com
3. Capture page title
4. Verify page loaded successfully
5. Close WebDriver session

**Expected Result**: 
- Page title displays "Example Domain"
- Page loads without errors
- Connection established successfully

**Postconditions**: Browser session properly terminated

---

### TS-002: Verify Page Title Display
**Objective**: Confirm page title is correctly retrieved and displayed

**Preconditions**:
- WebDriver initialized
- Navigation to example.com completed

**Test Steps**:
1. Get page title using `driver.getTitle()`
2. Log title to console
3. Verify title is not null or empty
4. Compare title with expected value

**Expected Result**: 
- Page title: "Example Domain"
- Title retrieved without exceptions
- Console output shows correct title

**Postconditions**: Title captured for logging

---

### TS-003: Verify Page URL After Navigation
**Objective**: Confirm correct URL is loaded after navigation

**Preconditions**:
- ChromeDriver initialized
- Navigation attempted

**Test Steps**:
1. Navigate to https://example.com
2. Get current URL using `driver.getCurrentUrl()`
3. Compare with expected URL
4. Verify URL matches exactly

**Expected Result**: 
- Current URL: https://example.com/
- URL matches expected value
- No redirects occur

**Postconditions**: URL verified and logged

---

### TS-004: Browser Window Properties
**Objective**: Verify browser window is created with proper dimensions

**Preconditions**:
- ChromeDriver initialized

**Test Steps**:
1. Get window size using `driver.manage().window()`
2. Verify window width > 0
3. Verify window height > 0
4. Maximize window if needed
5. Verify maximized size

**Expected Result**: 
- Window size properly set
- Width and height positive values
- Window maximizes successfully

**Postconditions**: Window properties captured

---

## Test Scenario Category 2: Angular Form Interactions

### TS-005: Navigate to Angular Practice Form
**Objective**: Successfully navigate to Rahul Shetty Academy Angular practice form

**Preconditions**:
- ChromeDriver initialized
- Internet connectivity available

**Test Steps**:
1. Initialize WebDriver
2. Navigate to https://rahulshettyacademy.com/angularpractice/
3. Wait for page to load completely
4. Verify page URL matches exactly
5. Verify form elements are visible

**Expected Result**: 
- URL assertion passes
- Page loads completely
- Form elements visible on page
- No navigation errors

**Postconditions**: Form page ready for interaction

---

### TS-006: Verify Angular Form Elements Exist
**Objective**: Confirm all required form elements are present on the page

**Preconditions**:
- Navigated to Angular practice form page

**Test Steps**:
1. Locate name input field
2. Locate email input field
3. Locate checkbox elements
4. Locate radio buttons
5. Locate select dropdown
6. Locate submit button
7. Verify all elements are present

**Expected Result**: 
- All form elements found
- No StaleElementReferenceException
- Elements are visible to user
- Elements are interactable

**Postconditions**: Form elements mapped and verified

---

### TS-007: Fill Name Field
**Objective**: Successfully enter name in the form name field

**Preconditions**:
- Angular form page loaded
- Name input field located

**Test Steps**:
1. Locate name input field
2. Clear any existing text
3. Type test name: "John Doe"
4. Verify text entered correctly
5. Capture field value

**Expected Result**: 
- Text "John Doe" entered successfully
- Field displays entered text
- No input errors occur

**Postconditions**: Name field populated

---

### TS-008: Fill Email Field
**Objective**: Successfully enter email address in the form email field

**Preconditions**:
- Angular form page loaded
- Email input field located

**Test Steps**:
1. Locate email input field
2. Clear any existing text
3. Type test email: "john.doe@example.com"
4. Verify email entered correctly
5. Check for email validation

**Expected Result**: 
- Email "john.doe@example.com" entered successfully
- Field displays entered email
- Email format accepted by form

**Postconditions**: Email field populated

---

### TS-009: Select Radio Button
**Objective**: Successfully select a radio button from available options

**Preconditions**:
- Angular form page loaded
- Radio button elements located

**Test Steps**:
1. Locate radio button group
2. Identify available options
3. Select first radio button
4. Verify selection status
5. Confirm selected attribute is set

**Expected Result**: 
- Radio button selected
- Only one option selected
- Selected attribute reflects true state
- No errors during selection

**Postconditions**: Radio button selection confirmed

---

### TS-010: Select Checkbox
**Objective**: Successfully interact with checkbox elements

**Preconditions**:
- Angular form page loaded
- Checkbox elements located

**Test Steps**:
1. Locate checkbox element
2. Click checkbox to select
3. Verify checkbox is checked
4. Click again to deselect
5. Verify checkbox is unchecked

**Expected Result**: 
- Checkbox selected and deselected
- Checked attribute changes correctly
- No errors during interaction

**Postconditions**: Checkbox interaction verified

---

### TS-011: Select Option from Dropdown
**Objective**: Successfully select an option from dropdown/select element

**Preconditions**:
- Angular form page loaded
- Select dropdown located

**Test Steps**:
1. Locate select dropdown element
2. Use Select class to interact with dropdown
3. Select an option by value or text
4. Verify selected option displays correctly
5. Capture selected value

**Expected Result**: 
- Option selected from dropdown
- Selected text displays correctly
- No errors during selection

**Postconditions**: Dropdown selection verified

---

### TS-012: Submit Form Successfully
**Objective**: Successfully submit the form with valid data

**Preconditions**:
- All form fields filled with valid data
- Form ready for submission

**Test Steps**:
1. Locate submit button
2. Click submit button
3. Wait for form processing
4. Verify success message appears
5. Check for page redirect or confirmation

**Expected Result**: 
- Submit button clicked successfully
- Form submitted without errors
- Success message displays
- Form processing completes

**Postconditions**: Form submission completed

---

### TS-013: Verify Form Submission Response
**Objective**: Confirm proper response after form submission

**Preconditions**:
- Form successfully submitted

**Test Steps**:
1. Wait for response page to load
2. Capture current URL
3. Verify success message content
4. Check for submitted data confirmation
5. Verify page state changes

**Expected Result**: 
- Success page loads
- URL changes appropriately
- Success message displays
- Submitted data reflected in response

**Postconditions**: Response verified

---

## Test Scenario Category 3: Form Validation & Error Handling

### TS-014: Submit Form with Empty Fields
**Objective**: Verify form validation rejects empty required fields

**Preconditions**:
- Form page loaded
- Form fields empty

**Test Steps**:
1. Locate submit button
2. Click submit without filling fields
3. Wait for validation messages
4. Capture validation error messages
5. Verify form not submitted

**Expected Result**: 
- Form not submitted
- Validation error messages display
- Required field indicators shown
- User prevented from submitting

**Postconditions**: Validation errors captured

---

### TS-015: Submit Form with Invalid Email
**Objective**: Verify email format validation

**Preconditions**:
- Form page loaded

**Test Steps**:
1. Fill name field with valid data
2. Enter invalid email: "not-an-email"
3. Attempt form submission
4. Capture validation error
5. Verify form not submitted

**Expected Result**: 
- Email validation error displays
- Form not submitted
- Error message indicates invalid email format
- User can correct and resubmit

**Postconditions**: Email validation verified

---

### TS-016: Handle Navigation Errors
**Objective**: Verify proper error handling for failed navigation

**Preconditions**:
- Internet connectivity may be unstable

**Test Steps**:
1. Attempt navigation to invalid URL
2. Capture exception
3. Verify exception handling
4. Check for error logging
5. Verify WebDriver cleanup

**Expected Result**: 
- Exception properly caught
- Error logged appropriately
- WebDriver resources cleaned up
- No hanging sessions

**Postconditions**: Error handling verified

---

### TS-017: Handle Element Not Found Errors
**Objective**: Verify proper error handling when elements cannot be located

**Preconditions**:
- Form page loaded

**Test Steps**:
1. Attempt to locate non-existent element
2. Set timeout for element search
3. Capture NoSuchElementException
4. Verify exception handling
5. Check error recovery

**Expected Result**: 
- Exception properly caught
- Timeout respected
- Error message logged
- Script continues or fails gracefully

**Postconditions**: Element not found error handled

---

## Test Scenario Category 4: Data-Driven Testing

### TS-018: Fill Form with Multiple Data Sets
**Objective**: Test form with various valid data combinations

**Preconditions**:
- Form page loaded
- Test data prepared

**Test Data Sets**:
```
Dataset 1: Name: "John Doe", Email: "john@example.com"
Dataset 2: Name: "Jane Smith", Email: "jane@example.com"
Dataset 3: Name: "Bob Johnson", Email: "bob@example.com"
```

**Test Steps**:
1. For each dataset:
   - Navigate to form page
   - Fill form with dataset values
   - Submit form
   - Verify success
   - Capture results

**Expected Result**: 
- Form submitted successfully for each dataset
- All submissions processed correctly
- Success messages display
- No data cross-contamination

**Postconditions**: Data-driven test completed

---

### TS-019: Fill Form with Edge Case Data
**Objective**: Test form with boundary and edge case values

**Preconditions**:
- Form page loaded
- Test data prepared

**Test Data**:
```
Test: Very long name (255+ characters)
Test: Special characters in name (!@#$%^&*)
Test: International characters (Unicode)
Test: SQL injection attempts
Test: XSS payload attempts
```

**Test Steps**:
1. For each edge case:
   - Fill form with edge case data
   - Submit form
   - Capture result (accepted/rejected)
   - Verify security handling

**Expected Result**: 
- System handles edge cases safely
- Security checks function properly
- Data sanitized if accepted
- Attacks prevented

**Postconditions**: Edge case handling verified

---

### TS-020: Performance Test - Multiple Form Submissions
**Objective**: Verify system performance under multiple rapid submissions

**Preconditions**:
- Form page loaded
- Performance monitoring enabled

**Test Steps**:
1. Prepare 10 valid test datasets
2. Submit form rapidly with each dataset
3. Record response time for each submission
4. Monitor system resources
5. Verify all submissions succeed
6. Analyze performance metrics

**Expected Result**: 
- All 10 submissions successful
- Response times acceptable
- No timeouts occur
- System resources remain stable
- Performance metrics logged

**Postconditions**: Performance data captured

---

## Test Scenario Category 5: End-to-End Workflows

### TS-021: Complete User Journey - Form Interaction to Submission
**Objective**: Verify complete user workflow from form access to successful submission

**Preconditions**:
- Test environment ready

**Test Steps**:
1. Initialize WebDriver
2. Navigate to Angular practice form
3. Verify page loads
4. Fill all form fields with valid data
5. Select appropriate options
6. Review form before submission
7. Submit form
8. Verify success response
9. Capture success confirmation
10. Close browser session

**Expected Result**: 
- All steps execute successfully
- Form fully submitted
- Success confirmation received
- No errors during workflow
- Resources properly cleaned up

**Postconditions**: End-to-end workflow completed

---

### TS-022: Multiple Form Submissions in Single Session
**Objective**: Verify multiple form submissions in one browser session

**Preconditions**:
- WebDriver initialized

**Test Steps**:
1. Navigate to form page
2. Fill and submit form (iteration 1)
3. Verify success
4. Return to form page
5. Fill and submit form (iteration 2)
6. Verify success
7. Return to form page
8. Fill and submit form (iteration 3)
9. Verify all submissions successful

**Expected Result**: 
- Multiple submissions in same session
- Each submission independent
- No session state issues
- All submissions recorded correctly

**Postconditions**: Multi-submission session verified

---

## Test Scenario Category 6: Browser & Session Management

### TS-023: Browser Session Initialization
**Objective**: Verify proper WebDriver session initialization

**Preconditions**:
- Chrome installed

**Test Steps**:
1. Create ChromeDriver instance
2. Verify instance created successfully
3. Check browser window opened
4. Verify browser ready for commands
5. Verify capabilities set correctly

**Expected Result**: 
- ChromeDriver instance created
- Browser window displays
- Browser responsive to commands
- All capabilities properly set

**Postconditions**: Session initialized

---

### TS-024: Browser Session Cleanup
**Objective**: Verify proper resource cleanup after session

**Preconditions**:
- WebDriver session active

**Test Steps**:
1. Execute test operations
2. Call driver.quit()
3. Verify browser window closes
4. Check for orphaned processes
5. Monitor system resources

**Expected Result**: 
- Browser window closes
- All resources released
- No orphaned chromedriver processes
- System resources freed

**Postconditions**: Session cleaned up

---

### TS-025: Handle Browser Crash
**Objective**: Verify system recovers from browser crashes

**Preconditions**:
- WebDriver session active

**Test Steps**:
1. Start normal operations
2. Simulate or trigger browser crash
3. Attempt to catch exception
4. Implement recovery logic
5. Restart WebDriver if needed
6. Continue operations

**Expected Result**: 
- Crash detected properly
- Exception caught and logged
- Recovery attempted
- Resources cleaned up
- Session can be restarted

**Postconditions**: Crash recovery verified

---

## Test Scenario Category 7: Regression & Compatibility

### TS-026: Regression Test - Verify Existing Functionality
**Objective**: Confirm existing features continue to work after changes

**Preconditions**:
- Baseline functionality established
- Code changes deployed

**Test Steps**:
1. Run all basic navigation tests (TS-001 to TS-004)
2. Run all form interaction tests (TS-005 to TS-013)
3. Verify all tests pass
4. Compare results with baseline
5. Document any deviations

**Expected Result**: 
- All tests pass
- Results match baseline
- No functionality broken
- Regression test suite passes

**Postconditions**: Regression verified

---

### TS-027: Cross-Browser Compatibility (Chrome)
**Objective**: Verify functionality works in Chrome browser

**Preconditions**:
- Chrome browser latest version installed

**Test Steps**:
1. Configure WebDriver for Chrome
2. Run test suite
3. Monitor for browser-specific issues
4. Verify all tests pass in Chrome
5. Document browser version and results

**Expected Result**: 
- All tests pass in Chrome
- No Chrome-specific errors
- Functionality works as expected
- Performance acceptable

**Postconditions**: Chrome compatibility verified

---

## Test Scenario Category 8: Accessibility & Usability

### TS-028: Verify Form Accessibility
**Objective**: Ensure form elements are accessible to users

**Preconditions**:
- Form page loaded

**Test Steps**:
1. Verify all form labels present
2. Check for aria attributes
3. Verify tab order logical
4. Test keyboard navigation
5. Check color contrast
6. Verify form readable by screen readers

**Expected Result**: 
- All labels properly associated
- ARIA attributes present
- Tab order logical and functional
- Keyboard navigation works
- Sufficient color contrast
- Screen reader compatible

**Postconditions**: Accessibility verified

---

### TS-029: Verify Form User Experience
**Objective**: Ensure form is user-friendly and intuitive

**Preconditions**:
- Form page loaded

**Test Steps**:
1. Verify form layout is clear
2. Check field labels are descriptive
3. Verify error messages are helpful
4. Check validation feedback timing
5. Verify success messages clear
6. Test field focus management

**Expected Result**: 
- Layout clear and organized
- Labels descriptive and helpful
- Error messages guide users
- Feedback timely and relevant
- Success messages clear
- Focus properly managed

**Postconditions**: UX verified

---

## Test Execution & Reporting

### Test Suite Organization
- **Quick Smoke Tests**: TS-001, TS-005, TS-021
- **Functional Tests**: TS-002 to TS-013
- **Validation Tests**: TS-014 to TS-017
- **Data-Driven Tests**: TS-018 to TS-020
- **Full Regression**: TS-001 to TS-029

### Test Execution Command
```bash
mvn test
```

### Test Results Location
```
target/surefire-reports/
```

### Success Criteria
- All critical tests must pass (Smoke Tests)
- At least 90% of all tests must pass
- Zero security vulnerabilities
- Performance metrics within acceptable range
- No orphaned processes or resource leaks

---

## Maintenance & Updates

- Review test scenarios monthly
- Update with new features added
- Archive obsolete scenarios
- Track defects found through testing
- Continuously improve test coverage