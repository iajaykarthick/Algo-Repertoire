import os
import sys
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
output_files_path = 'leetcode-problems/problems'
question_text_xpath = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div'

isExist = os.path.exists(output_files_path)        
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(output_files_path)
    print("The new directory is created!")


URL = "https://leetcode.com/api/problems/algorithms/"
response = requests.get(URL)
data = response.json()
for question_stat in data['stat_status_pairs'][:10]:
    question = question_stat['stat']
    question_id = question['question_id']
    question_title = question['question__title']
    question_title_slug = question['question__title_slug']
    URL = f"https://leetcode.com/problems/{question_title_slug}"
    filename = f"{output_files_path}/{question_id}_{question_title.replace(' ', '_')}.md"
    driver.get(URL)
    
    timeout = 3
    try:
        element_present = EC.presence_of_element_located((By.XPATH, question_text_xpath))
        WebDriverWait(driver, timeout).until(element_present)
        element = driver.find_element(By.XPATH, question_text_xpath)
        question_text = element.get_attribute('innerHTML')
        
        # Writing to file
        with open(filename, "w") as file1:
            # Writing data to a file
            file1.write(question_text)
    except TimeoutException:
        print("Timed out waiting for page to load")

# Writing to file
with open("leetcode-problems/questions-fetcher/logtrace.log", "w") as file1:
    # Writing data to a file
    file1.write("test")

# write content to md file
driver.quit()