from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.python.org")
print(driver.title)
