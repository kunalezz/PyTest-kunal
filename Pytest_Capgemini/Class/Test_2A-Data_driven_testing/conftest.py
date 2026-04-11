'''
We are writing fixture code in this conftest file it will automatically going to run acc to marker
'''

from selenium.webdriver import Chrome, ChromeOptions
import pytest

@pytest.fixture(autouse=True)
def test_openChrome():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print("Opening Browser")
    yield driver
    print("Closing Browser")
    driver.quit()
