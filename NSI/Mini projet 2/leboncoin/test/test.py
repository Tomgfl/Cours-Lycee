from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import *
import requests

from bs4 import BeautifulSoup

ser = Service("chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)



driver = webdriver.Chrome(service=ser, options=op)
driver.delete_all_cookies()


driver.get("https://www.proxysite.com/")


