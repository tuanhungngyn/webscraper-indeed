#%%
import time
from packages.init_browser import init_browser, next_page
from packages.browser_using import decline_cookies, save_to_csv, id_number_declaration
from packages.scraping import parse_html_joblist


def main():
    job_title = input("What Job are you looking for? :")
    location = input("Where do you want to work? :")
    job_title = job_title.replace(" ", "+")
    location = location.replace(" ", "+")
    url = f"https://de.indeed.com/jobs?q={job_title}&l={location}"


    input_file = f"{job_title}_{location}.csv"
    id_number = id_number_declaration(input_file)
    page_number = 0
    browser = init_browser(url)

    while True:
        time.sleep(5)
        decline_cookies(browser, page_number)
        new_data, id_number = parse_html_joblist(browser, id_number)
        if new_data:
            save_to_csv(new_data, input_file)
            print(f"Saved {len(new_data)} new jobs to CSV.")
        else: 
            print("No new jobs found on this page.")
        
        if not next_page(browser):
            print("No more pages to navigate. Exiting...")
            break
        
        page_number += 1

    browser.quit()



if __name__ == "__main__":
    main()
#%%




