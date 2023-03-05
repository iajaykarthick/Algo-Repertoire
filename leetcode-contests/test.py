from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://leetcode.com/problems/longest-palindromic-substring/")
soup = BeautifulSoup(driver.page_source, "html.parser")

for div in soup.find_all('div', {"class": "_1l1MA"}):
    print(div.get_attribute('innerHTML'))
driver.quit()