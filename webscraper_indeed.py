#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time
import pandas as pd

job_title = input("What Job are you looking for? :")
location = input("Where do you want to work? :")
# Replace the the input with + so URL is properly working
job_title = job_title.replace(" ", "+")
location = location.replace(" ", "+")
url = f"https://de.indeed.com/jobs?q={job_title}&l={location}"

browser = webdriver.Chrome()
browser.get(url)
input_file = f"{job_title}_{location}.csv"

file_exists = os.path.exists(input_file)
if file_exists:
    df = pd.read_csv(input_file)
else:
    df = pd.DataFrame(columns=["ID", "Title", "Company", "Location", "Job Information"])

id_number = len(df) #if there is already an existing file to append
page_number = 0


while True:
    time.sleep(5)  #wait for the page to load every element

    if page_number == 0:
        try:
            cookies_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-reject-all-handler")) 
            )
            cookies_button.click()
            print("Cookies declined on the first page.")
        except Exception as e:  
            print("Cookies button not found on the first page:", str(e))
    else:
        try:
            
            overlay_close_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button > svg"))
            )
            overlay_close_button.click()
            print(f"Overlay closed on page {page_number + 1}.")
        except Exception as e:
            print(f"Overlay button not found on page {page_number + 1}:", str(e))

    html_source_code = browser.execute_script("return document.body.innerHTML;")
    html_soup = BeautifulSoup(html_source_code, "html.parser")
    jobs = html_soup.find_all(class_="css-5lfssm")
    
    #look if jobs are properly found
    print(f"Found jobs: {len(jobs)} on page {page_number + 1}")

    new_data = []

    #scrape out elements and go through every element      
    for job in jobs:

        #debugging cases
        #print("HTML: ", job.prettify())

        title_tag = job.find(lambda tag: tag.has_attr("title"))
        company = job.find("span", class_="css-92r8pb")
        location = job.find("div", class_="css-1p0sjhy")
        job_link_tag = job.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")

        #for debugging cases
        # print("Title: ", title_tag)
        # print("Company: ", company)
        # print("Location: ", location)
        # print("Job Information: ", job_link_tag)
        
        if title_tag and company and location and job_link_tag:
            relative_job_url = job_link_tag["href"]
            full_job_url = "de.indeed.com" + relative_job_url
            id_number += 1
            data = {
                "ID": id_number,
                "Title": title_tag.text.strip(),
                "Location": location.text.strip(),
                "Job Information": full_job_url
            }
            new_data.append(data)
            print("New jobs: ", data)
    
    if new_data:
        new_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_df], ignore_index=True)


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



df.to_csv(input_file, index=False)
browser.quit()

# %%
