import pytest
from get_test_data import get_test_data
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('userName, password', get_test_data())
def test_login(test_openChrome, userName, password):
    test_openChrome.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(userName)
    test_openChrome.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    test_openChrome.find_element(By.XPATH, '//input[@id="login-button"]').click()

    expected = "https://www.saucedemo.com/inventory.html"
    actual = test_openChrome.current_url
    assert expected == actual, "Login failed"