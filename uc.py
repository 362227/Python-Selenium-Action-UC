#安装:pip3.8 install undetected-chromedriver
#wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
#yum install -y google-chrome-stable_current_x86_64.rpm


from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import os
import sys
import requests
import urllib.request
import re
import subprocess

print("运行前先杀死chrome")
os.system("pkill -9 chrome")
os.system('killall chrome')


url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
response = requests.get(url).text


m = re.match(r'.+?"url\"\:\"(https\:\/\/[\s\S]{2,85}chromedriver-linux64.zip).*', response)
zip_url  = m.group(1)
print ("Chrome下载地址:" + zip_url)


os.system(f"curl -o chromedriver-linux64.zip {zip_url}")

print("解压chromedriver文件")
os.system("unzip -o chromedriver-linux64.zip -d /opt/")


chromedriver_version = subprocess.check_output("/opt/chromedriver-linux64/chromedriver --version", shell=True, text=True)
print("chromedriver版本:" + chromedriver_version)



