#https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
#https://chercher.tech/python/assertion-unittest-python-selenium
#https://www.parsehub.com/blog/what-is-web-scraping/

from selenium import webdriver
import unittest
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess
import os
import sys

display = Display(visible=0, size=(1920, 1080))  
display.start()

os.system('sudo bin/v2ray -config bin/sw.json &')
sleep(3)
cmd = ['curl', '-x', '127.0.0.1:1083', '-L', 'http://www.google.com']
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#print(result.stdout)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--proxy-server=http://127.0.0.1:1083')
options.add_argument('--enable-javascript') # 启用 JavaScript
options.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
options.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
options.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')           # 隐藏滚动条，应对一些特殊页面



# Create browser session
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)
driver.maximize_window()
# Navigate to the application home page
driver.get("https://www.instagram.com")

    #def test_search_by_text(self):
# Get the search box
#search_box = driver.find_element(By.NAME, "q")

# Enter keyword and send it
#search_box.send_keys("instagram")
#search_box.send_keys(Keys.RETURN)
#search_box.submit()

# Get the list of search results
#lists = driver.find_elements(By.LINK_TEXT, '0 cookies - Cookie Clicker - Orteil')
#no = len(lists)
#assertEqual(1, len(lists))
#searchresult = driver.find_elements(By.CSS_SELECTOR, "#search > div:nth-child(1)")
#expectedlink = "https://www.instagram.com/?hl=id"
#for result in searchresult:
    #thelink = result.find_elements(By.CSS_SELECTOR, "a")
    #for href in thelink:
        #listhref = href.get_attribute("href")
        #if expectedlink in listhref:
            #assertEqual(listhref, expectedlink, "There's no link with expected")
#print(lists)


username_input = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
password_input = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

username_str = sys.argv[1]
password_str = sys.argv[2]


username_input.send_keys(username_str)
password_input.send_keys(password_str)
login.click()

sleep(7)


# Navigate to the Messages Page
#message = driver.find_element(By.CLASS_NAME, '_aacl _aacp _adda _aacx _aada')
#message.click()
driver.get('https://www.instagram.com')
sleep(5)
page_source = driver.page_source
print(page_source)
with open('./ig.html', 'w', encoding='utf-8') as f:
    f.write(page_source)
#Not Now for Notifications
#notif = driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
#notif.click()

sleep(9)
#page_source = driver.page_source
#print(page_source)

driver.quit()
