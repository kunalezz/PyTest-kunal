import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestRegisterForm:

    #“This function is a reusable setup method.”
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demowebshop.tricentis.com/register")
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_fill_registration_form(self):

        # Select Gender
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'gender-male'))
        ).click()

        # First Name
        self.wait.until(EC.presence_of_element_located(
            (By.NAME, "FirstName"))
        ).send_keys("Kunal")

        # Last Name
        self.driver.find_element(By.NAME, "LastName").send_keys("Soni")

        # Email
        self.driver.find_element(By.NAME, "Email").send_keys("kunal123@gmail.com")

        # Password
        self.driver.find_element(By.NAME, "Password").send_keys("Test@123")

        # Confirm Password
        self.driver.find_element(By.NAME, "ConfirmPassword").send_keys("Test@123")

        # Register
        self.driver.find_element(By.ID, 'register-button').click()

        # Assertion
        assert "register" in self.driver.page_source.lower()