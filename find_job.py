from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def wait(classname):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, classname))
    )

PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"

driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.chickpt.com.tw/")

wait("layout-width")
close=driver.find_element_by_id("qrcodebar-pc-closebtn")
action=ActionChains(driver)
action.click(close)
action.perform()

for page in range(50):
    wait("layout-width")
    jobs=[]
    salary=[]
    wait("layout-width")
    jobs=driver.find_elements_by_class_name("job-info-title")
    salary=driver.find_elements_by_class_name("salary")
    for i in range(len(salary)):
        realSalary=salary[i].text[4:]
        if int(realSalary) > 180 and "時薪" in salary[i].text:
            print(jobs[i].text,salary[i].text)
    
    time.sleep(1)
    nextPage=driver.find_elements_by_class_name("next-page")
    action=ActionChains(driver)
    action.click(nextPage[0])
    action.perform()
    time.sleep(2)
    

driver.quit()