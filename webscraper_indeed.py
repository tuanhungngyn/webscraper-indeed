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
jobs[0].text
# %%
jobs[1].text
# %%
for job in jobs:
    title = job.text
    # location = job.find("div", class_="css-92r8pb")
    # company = job.find("span", class_="css-1p0sjhy")
    print(title.strip(), "\n")
    # print(location)
    # print(company)
    # print("\n")
    # company = job.find("span", class_="css-1p0sjhy")


# %%


#titles = browser.find_elements(By.CLASS_NAME, "title")
#company_element = browser.find_element(By.XPATH, "")
#location_element = browser.find_element(By.XPATH, "")
#tag_element = browser.find_element(By.XPATH, "")
titles
# %%





# %%
jobs[0].text
# %%
job_title = job.find('span', id='jobTitle-e8f1e8f5742797f5')
if job_title:
    print(job_title.text)
else:
    print("Erorr text not found")

# %%
