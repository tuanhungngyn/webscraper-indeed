from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd



def decline_cookies(browser, page_number):
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




def save_to_csv(data, input_file):
    file_exists = os.path.exists(input_file)
    if file_exists:
        print(f"File {input_file} exists. Reading the existing input file.")
        df_existing = pd.read_csv(input_file)
    else:
        print(f"File {input_file} does not exist. Creating a new file.")
        df_existing = pd.DataFrame(columns=["ID", "Title", "Company", "Location", "Job Information"])
        
    df_new = pd.DataFrame(data)
    print(f"New data frame: \n{df_new}")

    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    df_combined.drop_duplicates(subset=["Title", "Company"], keep='first', inplace=True)

    df_combined.to_csv(input_file, index=False)


def id_number_declaration(input_file):
    file_exists = os.path.exists(input_file)
    if file_exists:
        df = pd.read_csv(input_file)
        id_number = len(df)
        return id_number
    else:
        return 0

