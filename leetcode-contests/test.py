from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lxml import etree

options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://leetcode.com/contest/weekly-contest-334/")
soup = BeautifulSoup(driver.page_source, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('"//*[@id="contest-app"]/div/div/div[4]/div[1]/ul/li[1]')[0].text)
