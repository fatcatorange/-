from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


account=input("輸入dcard帳號:")
password=input("輸入dcard密碼:")
#開啟瀏覽器
def wait(classname):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, classname))
    )


PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"
driver=webdriver.Chrome(PATH)



#上dcard 搜尋大同大學
driver.get("https://www.dcard.tw/f")
login=driver.find_element_by_class_name("jjui6k-0")
login.click()
time.sleep(1)
login=driver.find_element_by_name("email")
login.send_keys(account)
login=driver.find_element_by_name("password")
login.send_keys(password)
login.send_keys(Keys.RETURN)


wait("dj0ioy-2")


search = driver.find_element_by_class_name("dj0ioy-2")
search.clear()
search.send_keys("大同大學")
search.send_keys(Keys.RETURN)

wait("sc-3yr054-1")

articles=driver.find_elements_by_class_name("tgn9uw-3")
count=0

for article in articles:
    print(article.text)
    basic="幻想文"
    title=article.text
    if(basic in title):
        article.click()
        time.sleep(2)
        report=driver.find_element_by_class_name("beivpC")
        report.click()
        time.sleep(1)
        report=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div/div[1]/div/button[4]")
        report.click()
        time.sleep(2)
        #report=driver.find_element_by_xpath('//*[@id="modal-id-27-body"]/form/div/label[7]')
        reportA=driver.find_elements_by_class_name("sc-1i97w32")
        report=reportA[6]
        report.click()
        time.sleep(2)
        #report=driver.find_element_by_xpath('//*[@id="modal-id-27"]/footer/div[2]')
        reportA=driver.find_elements_by_class_name("sc-cc9qbz")
        report=reportA[1]
        report.click()
        time.sleep(2)
        driver.back()

time.sleep(3)

#driver.quit()
