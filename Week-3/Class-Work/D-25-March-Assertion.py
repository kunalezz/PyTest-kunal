"""
This script demonstrates how to use assertions in Selenium.

Assertions are used to validate whether the actual result matches
the expected result. If the condition fails, the test case fails.
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# Create Chrome options object
o = ChromeOptions()

# Keep the browser open even after script execution (for debugging)
o.add_experimental_option("detach", True)

# Initialize Chrome WebDriver with options
driver = Chrome(options=o)

# Maximize browser window for better visibility
driver.maximize_window()


# GOOGLE TEST
"""
# Open Google homepage
driver.get("https://google.com")

# Expected title of the page
expected = "Google"

# Fetch actual title from browser
actual = driver.title

# Assertion to validate page title
# If mismatch occurs, test fails with message
assert expected == actual, "Title mismatch"

# Locate search box and send input
driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("hehehe")
"""


#  AMAZON TEST

# Open Amazon India website
driver.get("https://amazon.in/")

# Apply implicit wait (wait up to 100 seconds for elements to load)
driver.implicitly_wait(100)

# Click on "Bestsellers" link using XPath
driver.find_element(By.XPATH, '//a[.="Bestsellers"]').click()

# Expected page title after navigation
expected = "Amazon.in Bestsellers: The most popular items on Amazon"

# Fetch actual page title
actual = driver.title

# Assertion to verify correct navigation
# If titles do not match, test will fail
assert expected == actual, "Title mismatch"

# Print message if assertion passes
print("Test Passed: Successfully navigated to Bestsellers page")

# Wait for 5 seconds to observe result
sleep(5)

# Close the browser
driver.quit()