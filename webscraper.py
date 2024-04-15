# %%
from bs4 import BeautifulSoup
import requests

url = "https://remote.co/remote-jobs/developer/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

results = soup.find("div", class_="card bg-light mb-3 rounded-0")
# %%
listing = results.find("div", class_="card-body p-0")
# %%
job_elements = listing.find("div", class_="col position-static")

# %%
for job_element in job_elements:
    title_element = job_elements.find("span", class_="font-weight-bold larger")
    date_element = job_elements.find("date")
    company_element = job_elements.find("p", class_="m-0 text-secondary")
    secondary_elements = listing.find(class_="badge badge-success")
    print(title_element.text.strip())
    print(date_element.text.strip())
    print(company_element.text.strip())
    print(secondary_elements.text)
    # %%
