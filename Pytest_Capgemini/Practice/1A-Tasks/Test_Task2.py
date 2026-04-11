import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--headless")
driver = Chrome(options=o)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/tables")

@pytest.mark.smoke
def test_dueAmt():
    dueAmt = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[2]').text

    expected = "$50.00"
    actual = dueAmt
    assert expected == actual

    print(f"Due amount - {dueAmt}")

@pytest.mark.smoke
def test_lastName():
    lastName = driver.find_element(By.XPATH, '//td[text()="Tim"]//preceding-sibling::td[1]').text

    expected = "Conway"
    actual = lastName
    assert expected == actual

    print(f"LastName - {lastName}")

@pytest.mark.regression
def test_email():
    email = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[1]').text

    actual = "tconway@earthlink.net"
    expected = email
    assert expected == actual

    print(f"Email - {email}")

@pytest.mark.regression
def test_website():
    website = driver.find_element(By.XPATH, '//td[text()="Tim"]//following-sibling::td[3]').text

    actual = "http://www.timconway.com"
    expected = website
    assert expected == actual

    print(f"Website - {website}")


'''
For smoke testing run -> pytest .\Test_Task2.py -vs -m "smoke"
For regression testing run -> pytest .\Test_Task2.py -vs -m "regression"
'''


