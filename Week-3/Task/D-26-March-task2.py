"""
This script demonstrates how to:
1. Open a website using Selenium
2. Capture a full-page screenshot
3. Capture a screenshot of a specific element (image)

Website used: Pinterest (homepage)
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# Create Chrome options
o = ChromeOptions()

# Keep browser open after script execution (useful for debugging)
o.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = Chrome(options=o)

# Maximize browser window
driver.maximize_window()

# Open Pinterest homepage
driver.get("https://in.pinterest.com/")

# Apply implicit wait (wait up to 100 seconds for elements to load)
driver.implicitly_wait(100)


# FULL PAGE SCREENSHOT

# Capture screenshot of the entire visible page
# File will be saved in current working directory
driver.save_screenshot("pageScreenshot.png")


# ELEMENT SCREENSHOT

# Locate a specific image element using XPath (based on 'src' attribute)
picture = driver.find_element(
    By.XPATH,
    '//img[@src="https://s.pinimg.com/webapp/visual-search-1px-ecc706bc.png"]'
)

# Capture screenshot of only the selected element
# Saves image as "picScreenshot.png"
picture.screenshot("picScreenshot.png")


# CLEANUP

# Wait for 5 seconds to observe the result
sleep(5)

# Close the browser
driver.quit()