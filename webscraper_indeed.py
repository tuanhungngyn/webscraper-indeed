# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time


browser = webdriver.Chrome()
browser.get("https://de.indeed.com/jobs?q=werkstudent+Informatik&l=Hamburg&from=searchOnHP&vjk=74a581fd64741df8")
html_source_code = browser.execute_script("return document.body.innerHTML;")
html_soup = BeautifulSoup(html_source_code, "html.parser")
jobs = html_soup.find_all(class_= "css-5lfssm")


with open("job_listing.csv", "w", newline="") as file:
    writer = csv.writer(file)
    header = ["Title", "Company", "Location"]
    writer.writerow(header)

    while True:
        time.sleep(5)
        for job in jobs:
            title_tag = job.find(lambda tag: tag.has_attr("title"))
            if title_tag:
                print(title_tag.text)
            else:
                continue
            company = job.find("span", class_="css-92r8pb")
            if company:
                print(company.text)
            else:
                continue
            location = job.find("div", "css-1p0sjhy")
            if location:
                print(location.text)
            else:
                continue
            print("\n")
            data = [title_tag.text, company.text, location.text]
            writer.writerow(data)
        try:
            next_button = browser.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[5]/div/div[1]/nav/ul/li[5]/a")
            if next_button:
                next_button.click()
        except Exception as e:
            print("Failed to click on the next button or end of pages", str(e))
            break



browser.quit()

# %%
