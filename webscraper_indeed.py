#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

job_title = input("What Job are you looking for? :")
location = input("Where do you want to work? :")
# Replace the the input with + so URL is properly working
job_title = job_title.replace(" ", "+")
location = location.replace(" ", "+")
url = f"https://de.indeed.com/jobs?q={job_title}&l={location}"

browser = webdriver.Chrome()
browser.get(url)

with open("job_listing.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Job Information"])
    
    page_number = 0  

    while True:
        time.sleep(5)  

        if page_number == 0:
            try:
                cookies_button = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-reject-all-handler"))  # Update your actual selector here
                )
                cookies_button.click()
                print("Cookies declined on the first page.")
            except Exception as e:
                print("Cookies button not found on the first page:", str(e))
        else:
            try:
                
                overlay_close_button = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button > svg"))  # Update your actual selector here
                )
                overlay_close_button.click()
                print(f"Overlay closed on page {page_number + 1}.")
            except Exception as e:
                print(f"Overlay button not found on page {page_number + 1}:", str(e))

        html_source_code = browser.execute_script("return document.body.innerHTML;")
        html_soup = BeautifulSoup(html_source_code, "html.parser")
        jobs = html_soup.find_all(class_="css-5lfssm")

        
        for job in jobs:
            title_tag = job.find(lambda tag: tag.has_attr("title"))
            company = job.find("span", class_="css-92r8pb")
            location = job.find("div", class_="css-1p0sjhy")
            job_link_tag = job.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")
            if title_tag and company and location and job_link_tag:
                job_url = job_link_tag["href"]
                data = [title_tag.text.strip(), company.text.strip(), location.text.strip(), job_url]
                writer.writerow(data)
                print(data)

        # Turning to next page
        try:
            next_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-label, 'Next Page')]"))
            )
            next_button.click()
            page_number += 1  # Increment the page counter after successfully clicking the next button
            print(f"Navigated to page {page_number + 1}.")
        except Exception as e:
            print("Failed to click on the next button or end of pages:", str(e))
            break

browser.quit()

# %%
