from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import random



def get_url(position, location):
    
    template = "https://www.indeed.ca/jobs?q={}&l={}&sort=date"
    url = template.format(position.replace(' ', '+'),
                          location.replace(' ', '+'))
    print(url)
    return url

def get_job_data(driver, target_url):
    driver.get(target_url)
    time.sleep(random.uniform(8.5, 10.9))
    try:
        close = driver.find_element('xpath', '//*[@id="mosaic-desktopserpjapopup"]/div[1]/button')
        close.click()
    except:
        pass


    all_data = []

    job_cards = driver.find_elements('xpath', '//div[@class = "css-1m4cuuf e37uo190"]' )

    for card in job_cards:
        card.location_once_scrolled_into_view
        card.click()
        time.sleep(random.uniform(4.6, 6.9))
   
        job_title = driver.find_element('xpath', '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div/div/div[1]/div/div[1]/div[1]/h2' ).text.strip()
        title = job_title.split('\n')
        data = {'Job Title': title}
        all_data.append(data)
    print(all_data)


def main():
    # PROXY = ""
    # chrom_options = webdriver.ChromeOptions()
    # chrom_options.add_argument(f'--proxy-server={PROXY}')
    position = 'Software Engineer Intern'
    location = 'Vancouver, BC'
    jobs = []
    url =get_url(position, location)
    browser = webdriver.Chrome()
    for page in range(0, 50, 10):
        order_page = (url + '&start=' +str(page))
        browser.get(order_page)
        time.sleep(random.uniform(2, 4))
        # We need to add close modal button just in case if theres notifications popped out
        get_job_data(browser, order_page)

    browser.close()



main()
