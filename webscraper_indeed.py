# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            company = job.find("span", class_="css-92r8pb")
            location = job.find("div", "css-1p0sjhy")
            if title_tag and company and location:
                print(title_tag.text)
                print(company.text)
                print(location.text)
                print("\n")
            else:
                continue
            data = [title_tag.text, company.text, location.text]
            writer.writerow(data)
        try:
            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable ((By.XPATH, "//a[contains(@aria-label, 'Next Page')]"))
            )
            next_button.click()
        except Exception as e:
            print("Failed to click on the next button or end of pages:", str(e))
            raise
            break


browser.quit()

# %%
