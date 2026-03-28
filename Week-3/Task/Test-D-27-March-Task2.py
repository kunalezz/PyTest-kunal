from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
o = ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)
driver.implicitly_wait(20)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()

driver.find_element(By.XPATH,'//a[@href="/apparel-shoes"]').click()

sortBy = driver.find_element(By.XPATH,"//select[@id='products-orderby']")
dd1 = Select(sortBy)
dd1.select_by_value('https://demowebshop.tricentis.com/apparel-shoes?orderby=11')

display = driver.find_element(By.XPATH,"//select[@id='products-pagesize']")
dd2 = Select(display)
dd2.select_by_index(2)

view_as = driver.find_element(By.XPATH,"//select[@id='products-viewmode']")
dd3 = Select(view_as)
dd3.select_by_visible_text('List')

sleep(2)
driver.quit()