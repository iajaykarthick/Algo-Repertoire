from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lxml import etree

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://leetcode.com/contest/weekly-contest-334/")
soup = BeautifulSoup(driver.page_source, "html.parser")
links = []

for li in soup.find_all('ul', {"class": "list-group hover-panel contest-question-list"})[0].find_all("li", {"class": "list-group-item"}):
    for a in li.find_all('a'):
        links.append(a['href'])
        
for link in links:
    URL = 'https://leetcode.com' + link
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup.title)
driver.quit()