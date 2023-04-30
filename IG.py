#https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
#https://chercher.tech/python/assertion-unittest-python-selenium
#https://www.parsehub.com/blog/what-is-web-scraping/

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import subprocess
import os

subprocess.Popen(['sudo', 'bin/v2ray', '-config bin/sw.json'])
sleep(3)
cmd = ['curl', '-x', '127.0.0.1:1083', '-L', 'http://www.google.com']
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--proxy-server=http://127.0.0.1:1083')
options.add_argument('--enable-javascript') # 启用 JavaScript
options.add_argument('blink-settings=imagesEnabled=false')      # 不加载图片，提升运行速度
options.add_argument('--no-sandbox')                # 解决DevToolsActivePort文件不存在的报错
options.add_argument('--disable-gpu')               # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')           # 隐藏滚动条，应对一些特殊页面


class CookieClickerTest(unittest.TestCase):

    def setUp(self):
        # Create browser session
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        # Navigate to the application home page
        self.driver.get("https://www.instagram.com")

    #def test_search_by_text(self):
        # Get the search box
        #self.search_box = self.driver.find_element(By.NAME, "q")
        
        # Enter keyword and send it
        #self.search_box.send_keys("instagram")
        #self.search_box.send_keys(Keys.RETURN)
        #self.search_box.submit()

        # Get the list of search results
        #lists = self.driver.find_elements(By.LINK_TEXT, '0 cookies - Cookie Clicker - Orteil')
        #no = len(lists)
        #self.assertEqual(1, len(lists))
        #searchresult = self.driver.find_elements(By.CSS_SELECTOR, "#search > div:nth-child(1)")
        #expectedlink = "https://www.instagram.com/?hl=id"
        #for result in searchresult:
            #thelink = result.find_elements(By.CSS_SELECTOR, "a")
            #for href in thelink:
                #listhref = href.get_attribute("href")
                #if expectedlink in listhref:
                    #self.assertEqual(listhref, expectedlink, "There's no link with expected")
        #print(lists)
        

    def test_login(self):
        self.username = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
        self.password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        self.login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

        username = os.environ['IG_NAME']
        password = os.environ['IG_PW']
        
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login.click()

        sleep(9)

        # Navigate to the Messages Page
        #self.message = self.driver.find_element(By.CLASS_NAME, '_aacl _aacp _adda _aacx _aada')
        #self.message.click()
        self.driver.get('https://www.instagram.com')
        #Not Now for Notifications
        self.notif = self.driver.find_element(By.XPATH, '//button[contains(text(), "以后再说")]')
        self.notif.click()

        sleep(9)
        page_source = self.driver.page_source
        print(page_source)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

#1. test search by text
#2. test login on the homepage
#3. test send message
#    a. Messages
#       > New Message
#         > Type name
#           > Type text message
#           > send
# https://medium.com/analytics-vidhya/making-an-instagram-bot-using-selenium-and-python-ea94f217d0dd
# https://www.datacamp.com/tutorial/git-push-pull
