import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

@pytest.mark.parametrize('userName, password', [('standard_user', 'secret_sauce'), ('ajjjj0', 'secret_se')])
def test_login(userName, password):
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(userName)
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//input[@id="login-button"]').click()

    expected = "https://www.saucedemo.com/inventory.html"
    actual = driver.current_url
    assert expected == actual, "Login failed"