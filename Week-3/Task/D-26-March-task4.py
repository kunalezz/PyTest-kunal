"""
This script demonstrates:
1. Searching for a product on Amazon
2. Selecting a suggestion from auto-suggest dropdown
3. Applying sorting and filters
4. Extracting product name and price

Use case: Basic web scraping + automation flow
"""

import os
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
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

# Open Amazon India website
driver.get("https://www.amazon.in/")

# Apply implicit wait (wait up to 100 seconds for elements)
driver.implicitly_wait(100)


# SEARCH PRODUCT

# Locate search box and enter "mobiles"
driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys("mobiles")

# Wait for suggestions to load
sleep(2)

# Select one of the auto-suggestions (4th row)
driver.find_element(By.XPATH, '//div[@aria-rowindex="4"]').click()


# SORTING

# Click on sorting dropdown
driver.find_element(By.XPATH, '//span[@class="a-dropdown-label"]').click()

# Select "Newest Arrivals" option
driver.find_element(By.XPATH, '//a[.="Newest Arrivals"]').click()


# APPLY FILTER

# Apply "Free Shipping" filter
driver.find_element(By.XPATH, '//span[.="Free Shipping"]').click()


# EXTRACT DATA

# Get name of the first product in the results
name = driver.find_element(By.XPATH, '(//div[@data-cy="title-recipe"])[1]').text

# Get price of the first product
price = driver.find_element(By.XPATH, '(//span[@class="a-price-whole"])[1]').text


# OUTPUT

# Print extracted product details
print(f"Name - {name}")
print(f"Price - {price}")