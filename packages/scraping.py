from bs4 import BeautifulSoup


def parse_html_joblist(browser, id_number):
    html_source_code = browser.execute_script("return document.body.innerHTML;")
    html_soup = BeautifulSoup(html_source_code, "html.parser")
    jobs = html_soup.find_all(class_="css-5lfssm")
     
    new_data = []

    #look if jobs are properly found
    print(f"Found jobs: {len(jobs)} on current page")
     
    for job in jobs:

        #debugging cases
        print("HTML: ", job.prettify())
        title_tag = job.find(lambda tag: tag.has_attr("title"))
        company = job.find("span", class_="css-92r8pb")
        location = job.find("div", class_="css-1p0sjhy")
        job_link_tag = job.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")

        #for debugging cases
        #print("Title: ", title_tag)
        #print("Company: ", company)
        #print("Location: ", location)
        #print("Job Information: ", job_link_tag)
        
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
            
    return new_data, id_number
