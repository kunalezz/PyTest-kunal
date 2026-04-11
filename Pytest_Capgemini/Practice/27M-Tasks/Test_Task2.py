from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/apparel-shoes")

driver.implicitly_wait(100)

def test_orderBy():
    dropdown1 = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
    option1 = Select(dropdown1)
    option1.select_by_visible_text("Price: High to Low")

def test_pageSize():
    dropdown2 = driver.find_element(By.XPATH, '//select[@id="products-pagesize"]')
    option2 = Select(dropdown2)
    option2.select_by_visible_text("12")

def test_viewMode():
    dropdown3 = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
    option3 = Select(dropdown3)
    option3.select_by_visible_text("List")

sleep(5)
driver.quit()