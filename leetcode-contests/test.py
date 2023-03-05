from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lxml import etree

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://leetcode.com/contest/weekly-contest-334/")
soup = BeautifulSoup(driver.page_source, "html.parser")
for li in soup.find_all('ul', {"class": "list-group hover-panel contest-question-list"})[0].find_all("li"):
    print(li)
driver.quit()