import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#from selenium.webdriver.common.by import By

ser = Service("chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument('window-size=0x0')
driver = webdriver.Chrome(service=ser, options=op)

url = "https://fr-fr.facebook.com/marketplace/search/?query=samsung"
driver.get(url)

temp_html = driver.page_source
temp_soup = BeautifulSoup(temp_html,'lxml')
temp_items = temp_soup.findAll("div",{"class":"b3onmgus ph5uu5jm g5gj957u buofh1pr cbu4d94t rj1gh0hx j83agx80 rq0escxv fnqts5cd fo9g3nie n1dktuyu e5nlhep0 ecm0bbzt"})


page_state = driver.execute_script('return document.readyState;')
print(page_state)


#a = driver.find_element(By.XPATH,"//div[contains(@class, 'b3onmgus ph5uu5jm g5gj957u buofh1pr cbu4d94t rj1gh0hx j83agx80 rq0escxv fnqts5cd fo9g3nie n1dktuyu e5nlhep0 ecm0bbzt')]")
#print(a)

html = driver.page_source
#driver.quit()

soup = BeautifulSoup(html,'lxml')
items = soup.findAll("div",{"class":"b3onmgus ph5uu5jm g5gj957u buofh1pr cbu4d94t rj1gh0hx j83agx80 rq0escxv fnqts5cd fo9g3nie n1dktuyu e5nlhep0 ecm0bbzt"})
print(len(items))




