"""
This script demonstrates:
1. Performing login automation using Selenium
2. Validating navigation using assertions
3. Capturing a screenshot when test fails (Exception handling)

Use case: Negative test case (locked user login)
"""

import os
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# Create Chrome options
o = ChromeOptions()

# Keep browser open after execution (useful for debugging)
o.add_experimental_option("detach", True)

# Initialize WebDriver
driver = Chrome(options=o)

# Maximize browser window
driver.maximize_window()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Apply implicit wait (waits up to 100 seconds for elements to load)
driver.implicitly_wait(100)


# LOGIN ACTION

# Enter username (locked user for negative testing)
driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys("locked_out_user")

# Enter password
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("secret_sauc")

# Click login button
driver.find_element(By.XPATH, '//input[@id="login-button"]').click()


#  VALIDATION

# Expected URL after successful login
expected = "https://www.saucedemo.com/inventory.html"

# Get current URL after login attempt
actual = driver.current_url


# ASSERTION WITH EXCEPTION HANDLING

try:
    # Validate if login was successful
    assert expected == actual

except:
    # If assertion fails, capture screenshot for debugging
    # Screenshot helps identify UI errors or failure reasons
    driver.save_screenshot("screenshot1.png")


# CLEANUP

# Wait for 5 seconds to observe result
time.sleep(5)

# Close browser
driver.quit()