import pytest
from selenium import webdriver
from config.env import ConfigReader

@pytest.fixture
def setup_and_teardown():

    # Read config
    config = ConfigReader.read_config()
    env = config['qa']
    base_url = env['base_url']

    # Setup(Before test)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    yield driver  # Test runs here

    # Teardown (After test)
    driver.quit()
