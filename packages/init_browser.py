from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_browser(url):
     browser = webdriver.Chrome()
     browser.get(url)
     return browser


def next_page(browser):
    try:
        next_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@aria-label, 'Next Page')]"))
        )
        next_button.click()
        return True
    except Exception as e:
        print("Failed to click on the next button or end of pages:", str(e))
        return False