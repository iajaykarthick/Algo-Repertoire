from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://leetcode.com/problems/longest-palindromic-substring/")
soup = BeautifulSoup(driver.page_source, "html.parser")

# for div in soup.find_all('div', {"class": "list-group hover-panel contest-question-list"}):
#     print(div.get_attribute('innerHTML'))

print(soup.title)
element = driver.find_element(By.XPATH, '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div')
print(element.get_attribute('innerHTML'))
driver.quit()