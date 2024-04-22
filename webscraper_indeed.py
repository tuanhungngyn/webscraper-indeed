# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
browser.get("https://de.indeed.com/jobs?q=werkstudent+Informatik&l=Hamburg&from=searchOnHP&vjk=74a581fd64741df8")
html_source_code = browser.execute_script("return document.body.innerHTML;")
html_soup = BeautifulSoup(html_source_code, "html.parser")

jobs = html_soup.find_all(class_= "css-5lfssm")
# %%
jobs[0]
# %%
for job in jobs:

    title = job.find("span", class_= "title")
    print(title)
# %%
location = jobs.find("div", class_="css-92r8pb")
company = jobs.find("span", class_="css-1p0sjhy")
#titles = browser.find_elements(By.CLASS_NAME, "title")
#company_element = browser.find_element(By.XPATH, "")
#location_element = browser.find_element(By.XPATH, "")
#tag_element = browser.find_element(By.XPATH, "")
titles
# %%




