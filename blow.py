from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://tsj.tw/")

action=ActionChains(driver)

blow=driver.find_element_by_id("click")
blow_count=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
action.click(blow)

buy=[]
buy.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
buy.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))
buy.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

price=[]
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))


for i in range(100):
    action.perform()
    count=(int(blow_count.text.replace("您目前擁有","").replace("技術點","")))
    check=0
    for j in range(3):
        nowPrice=(int(price[j].text.replace("技術點","")))
        print(count,nowPrice,check)
        if count>=nowPrice:
            plus=ActionChains(driver)
            plus.click(buy[check])
            print("click",check)
            plus.perform()
            break
        check+=1
    time.sleep(1)

