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

print("密码："+sys.argv[2])
exit()
