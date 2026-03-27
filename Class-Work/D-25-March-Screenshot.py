"""
This script demonstrates how to take screenshots in Selenium:
1. Full page screenshot
2. Screenshot of a specific element
3. Screenshot with timestamp-based naming

It also shows how to dynamically create a folder to store screenshots.
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

# Open Google homepage
driver.get("https://google.com")

# Apply implicit wait (waits up to 100 seconds for elements)
driver.implicitly_wait(100)


# SCREENSHOT SETUP

# Create a folder named "screenshots" in current working directory
folder = os.path.join(os.getcwd(), "screenshots")

# Create folder if it does not already exist
os.makedirs(folder, exist_ok=True)


# FULL PAGE SCREENSHOT

# Take screenshot of the entire visible page
# This saves the screenshot as "screenshot1.png" inside screenshots folder
driver.save_screenshot(f"{folder}/screenshot1.png")


#  ELEMENT SCREENSHOT
# Locate a specific element using XPath
ele = driver.find_element(By.XPATH, '//div[@jscontroller="cnjECf"]')

# Take screenshot of only that element
# Saves image as "screenshot_ele.png"
ele.screenshot(f"{folder}/screenshot_ele.png")


# TIMESTAMP BASED SCREENSHOT

# Locate another element
ele2 = driver.find_element(By.XPATH, '//div[@class="vcVZ7d"]')

# Generate timestamp in format: YYYYMMDD - HHMMSS
timestamps = time.strftime("%Y%m%d - %H%M%S")

# Take screenshot with dynamic filename using timestamp
# Helps avoid overwriting previous screenshots
ele2.screenshot(f"{folder}/screenshot_ele_{timestamps}.png")


