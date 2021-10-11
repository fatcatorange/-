from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"
driver=webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
pop=driver.find_element_by_class_name("cat-img")
while True:
    try:
        pop.click()
        time.sleep(0.1)
    except:
        break
driver.quit()