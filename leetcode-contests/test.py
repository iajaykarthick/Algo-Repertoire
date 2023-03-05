import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://leetcode.com/problems/longest-palindromic-substring/")
question_text_xpath = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div'
timeout = 3
try:
    element_present = EC.presence_of_element_located((By.XPATH, question_text_xpath))
    WebDriverWait(driver, timeout).until(element_present)
    element = driver.find_element(By.XPATH, question_text_xpath)
    print(type(element.get_attribute('innerHTML')))
except TimeoutException:
    print("Timed out waiting for page to load")

# Writing to file
with open("leetcode-contests/test.log", "w") as file1:
    # Writing data to a file
    file1.write("test")

# write content to md file
driver.quit()