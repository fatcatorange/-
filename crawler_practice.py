
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#設定等待條件
def wait(classname):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, classname))
    )


#開啟瀏覽器
PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(PATH)

# driver = webdriver.Chrome(options=options)

#上dcard 搜尋大同大學
driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_class_name("dj0ioy-2")
search.clear()
search.send_keys("大同大學")
search.send_keys(Keys.RETURN)

wait("sc-3yr054-1")

#點進大同大學板
board=driver.find_element_by_class_name("bi971z-2")
print(board.text)
board.click()

wait("sc-5ro7wp-0")

#點進最新
title=driver.find_elements_by_class_name("pkcmwm-1")
for now in title:
    print(now.text)
    if(now.text=="最新"):
        now.click()
        break

wait("tgn9uw-3")
time.sleep(2)
#點入每篇文章
article=driver.find_elements_by_class_name("cTrcqd")
print(len(article))
print(article)
time.sleep(2)
for nowR in article:
    #print(nowR)
    nowR.click()
    wait("xrkql2-0")
    author=driver.find_element_by_class_name("xrkql2-0")
    print(author)
    if str(author.text)=="NNCCB":
        print("找到幻想文了!快檢舉!")
        exit()
    driver.back()

time.sleep(2)
# driver.quit()
