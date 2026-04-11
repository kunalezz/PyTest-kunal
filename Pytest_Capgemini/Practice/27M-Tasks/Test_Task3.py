from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

driver.implicitly_wait(10)

def test_scrollToFooterAndClick():
    footer = driver.find_element(By.XPATH, '//div[@class="footer-disclaimer"]')
    actions = ActionChains(driver)
    actions.scroll_to_element(footer).perform()
    sleep(2)
    driver.find_element(By.XPATH, '//a[.="Facebook"]').click()

def test_switchAndlogin():
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("hehe@gmail.com")
    driver.find_element(By.XPATH, '//input[@name="pass"]').send_keys("hehe@123")
    driver.find_element(By.XPATH, '(//span[.="Log in"])[6]').click()

# sleep(5)
# driver.quit()
