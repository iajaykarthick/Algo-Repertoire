from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://leetcode.com/contest/weekly-contest-334/")
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup)
