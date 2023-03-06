import os
import time
import sys
import requests

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

def find(driver):
    element = driver.find_element(By.XPATH, question_text_xpath)
    if element:
        return element
    else:
        return False

options = Options() 
options.add_argument("-headless") 
output_files_path = 'leetcode-problems/problems'
question_text_xpath = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div'

isExist = os.path.exists(output_files_path)        
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(output_files_path)
    print("problems directory created")
probs_number = [file.split("_")[0] for file in os.listdir(output_files_path)]

URL = "https://leetcode.com/api/problems/algorithms/"
response = requests.get(URL)
data = response.json()

for question_stat in data['stat_status_pairs'][:200]:
    question = question_stat['stat']
    question_id = question['question_id']
    if str(question_id) in probs_number:
        print(f"{question_id} already exists")
        continue
    question_title = question['question__title']
    question_title_slug = question['question__title_slug']
    URL = f"https://leetcode.com/problems/{question_title_slug}"
    filename = f"{output_files_path}/{question_id}_{question_title.replace(' ', '_')}.md"
    
    # driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver", options=options)
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.get(URL)
    timeout = 4
    try:
        element_present = EC.presence_of_element_located((By.XPATH, question_text_xpath))
        WebDriverWait(driver, timeout).until(element_present)
        
        element = WebDriverWait(driver, 5).until(find)
        
        
        question_text = element.get_attribute('innerHTML')
        
        # Writing to file
        with open(filename, "w") as file1:
            # Writing data to a file
            file1.write(f"## {question_title}\n")
            file1.write(f"[Leetcode]({URL})\n")
            file1.write(question_text)
            
    except TimeoutException:
        print("Timed out waiting for page to load")
        
    driver.close()
    time.sleep(2)

# Writing to file
with open("leetcode-problems/questions-fetcher/logtrace.log", "w") as file1:
    # Writing data to a file
    file1.write("test")
