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

timeout = 3
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    element = driver.find_element(By.XPATH, '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div')
    print(element.get_attribute('innerHTML'))

driver.get("https://leetcode.com/problems/longest-palindromic-substring/")
timeout = 10
topics_xpath = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[8]/div'
try:
    element_present = EC.presence_of_element_located((By.XPATH, topics_xpath))
    WebDriverWait(driver, timeout).until(element_present)
    print("Page loaded")
    element = driver.find_element(By.XPATH, topics_xpath)
    print(element.get_attribute('innerHTML'))
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    

driver.quit()