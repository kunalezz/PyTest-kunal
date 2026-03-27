"""
This script demonstrates:
1. Navigation and validation using Selenium
2. Handling hover issues using ActionChains
3. Working with dropdowns using Select class
4. Taking screenshots for verification

Website used: Lenskart
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create Chrome options
o = ChromeOptions()

# Keep browser open after execution (useful for debugging)
o.add_experimental_option("detach", True)

# Initialize WebDriver
driver = Chrome(options=o)

# Maximize browser window
driver.maximize_window()

# Open Lenskart website
driver.get("https://www.lenskart.com/")

# Apply implicit wait (wait up to 100 seconds for elements)
driver.implicitly_wait(100)


# NAVIGATION

# Click on "EYEGLASSES" menu
driver.find_element(By.XPATH, '//a[.="EYEGLASSES"]').click()

# Expected URL after clicking
expected = "https://www.lenskart.com/eyeglasses.html"

# Get current URL
actual = driver.current_url

# Validate navigation using assertion
assert expected == actual, "Error: Navigation failed"


# HANDLE HOVER ISSUE

"""
After clicking, sometimes a hover menu remains active (e.g., from navbar),
which blocks visibility of elements below.

To resolve this, we move the mouse pointer to another element.
"""

# Locate a safe element to move mouse (e.g., "Corporate")
toRemoveMousePtr = driver.find_element(By.XPATH, '//a[.="Corporate"]')

# Create ActionChains object
actions = ActionChains(driver)

# Move mouse to the selected element to remove hover overlay
actions.move_to_element(toRemoveMousePtr).perform()


# DROPDOWN HANDLING

# Locate dropdown element (Sort By)
dropdown = driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]')

# Create Select object to interact with dropdown
option = Select(dropdown)

# Select option by value (sorting by "popular")
option.select_by_value("popular")


# SCREENSHOT

# Capture screenshot after performing actions
driver.save_screenshot("screenshot.png")


# CLEANUP

# Wait for 5 seconds to observe result
sleep(5)

# Close browser
driver.quit()