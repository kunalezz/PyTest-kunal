import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

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

@pytest.mark.parametrize('userName, password', [('standard_user', 'secret_sauce'), ('locked_out_user', 'secret_sauce')])
def test_login(test_openChrome, userName, password):
    test_openChrome.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(userName)
    test_openChrome.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    test_openChrome.find_element(By.XPATH, '//input[@id="login-button"]').click()

    expected = "https://www.saucedemo.com/inventory.html"
    actual = test_openChrome.current_url
    assert expected == actual, "Login failed"