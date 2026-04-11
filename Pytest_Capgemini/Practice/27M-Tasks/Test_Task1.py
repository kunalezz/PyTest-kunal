from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

driver.implicitly_wait(10)

def test_register():
    driver.find_element(By.XPATH, '//a[.="Register"]').click()

def test_gender():
    driver.find_element(By.XPATH, '//input[@id="gender-male"]').click()

def test_firstName():
    driver.find_element(By.XPATH, '//input[@id="FirstName"]').send_keys("Ram")

def test_lastName():
    driver.find_element(By.XPATH, '//input[@id="LastName"]').send_keys("Krishn")

def test_email():
    driver.find_element(By.XPATH, '//input[@id="Email"]').send_keys("Krishn@gmail.com")

def test_password():
    driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys("@123456")

def test_cPassword():
    driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]').send_keys("@123456")

def test_regBtn():
    driver.find_element(By.XPATH, '//input[@id="register-button"]').click()
