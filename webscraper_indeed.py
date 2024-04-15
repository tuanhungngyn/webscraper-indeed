# %%
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
browser.get("https://de.indeed.com/jobs?q=werkstudent+Informatik&l=Hamburg&from=searchOnHP&vjk=74a581fd64741df8")

title_element = browser.find_element(By.XPATH, "/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[1]/div/div/div/div/div/table[1]/tbody/tr/td[1]/div[1]/h2/a/span")
##titles = [title.text for title in title_element]
#company_element = browser.find_element(By.XPATH, "")
#location_element = browser.find_element(By.XPATH, "")
#tag_element = browser.find_element(By.XPATH, "")
browser.quit()
title_element.text
# %%




