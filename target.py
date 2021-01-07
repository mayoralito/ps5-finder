import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pickle
import time
from datetime import datetime
from time import gmtime, strftime

import os

from email_helpers import build_email_content_not_found_to, build_email_content_found_to

def ps5_search_for_stock(email_to):
    script_start_at = datetime.now()
    current_time = strftime("%Y-%m-%d_%H:%M", gmtime())
    print("Script started at: ", current_time, ":D")

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1600,1200")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service('chromedriver')
    print("Configuring driver via Service")
    service.start()
    driver = webdriver.Remote(
        command_executor=service.service_url, 
        desired_capabilities = {'browserName': 'chrome'},
        options=chrome_options
    )

    driver.implicitly_wait(5)

    source_url = 'https://www.target.com/'
    driver.get(source_url)
    print("Getting address " + source_url)
    # driver.get('https://www.target.com/p/playstation-5-console/-/A-81114595')

    search_input = driver.find_elements_by_css_selector("input[name=\"searchTerm\"]")[0]    
    time.sleep(1)

    search_term = "ps5 console"
    search_input.send_keys(search_term)
    print("Searching term " + search_term)
    time.sleep(1)

    # checkbox = driver.find_elements_by_css_selector("div.icheckbox")[0]
    # checkbox.click()
    # time.sleep(2)


    # login_button = driver.find_element_by_xpath('//*[@id="new_user"]/p[1]/input')
    # login_button.click()
    # time.sleep(5)

    print("Trying to submit()")
    search_form = driver.find_element_by_xpath('//*[@id="search"]')
    search_form.submit()
    time.sleep(3)

    # https://selenium-python.readthedocs.io/waits.html#implicit-waits
    # driver.implicitly_wait(7) # seconds
    # Find a way to do implicit wait if the page has been reloaded.

    print("Trying to get clickable element to display overlay.")
    ps5_element = driver.find_element_by_xpath('//*[@id="mainContainer"]/div[2]/div[1]/a[1]')
    ps5_element.click()
    time.sleep(2)

    # This works
    # ps5_overlay_close_button = driver.find_elements_by_css_selector('.LayoutCloseButton__CloseButton-sc-1s4jhd1-1.bwYwmv')[0]
    # ps5_overlay_close_button.click()
    # time.sleep(3)

    
    # ps5_overlay_close_button = driver.find_elements_by_css_selector('ul[data-test="shoppableDrawer-productList"]')[0]
    # ps5_overlay_first_item_button = driver.find_element_by_xpath('//*[@data-test="shoppableDrawer-productList"]/li[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/')
    # ps5_overlay_first_item_button = driver.find_element_by_xpath('//*[@data-test="addButton"]')
    print("Diving into overlay options AND click()")
    ps5_overlay_first_item_button = driver.find_elements_by_css_selector('.overlay--opened.overlay button[data-test="addButton"]')[1]
    ps5_overlay_first_item_button.click()
    time.sleep(2)

    # Check for current store
    print("Checking storeAvailabilityStoreCard")
    ps5_current_store = driver.find_elements_by_css_selector('div[data-test="storeAvailabilityStoreCard"]')
    time.sleep(1)

    # print(ps5_current_store)
    # ps5_current_name = ps5_current_store[2]
    # print(ps5_current_name)
    store_count = 0
    file_name =  "/tmp/latest-scan.txt"
    print("Writing latest scan on " + file_name)
    with open(file_name, "w") as text_file:
        text_file.write("\n-------------\n[INI::AUTO-GENERATED REPORT] - %s" % (current_time))
        print("Processing ps5_current_store content, current items: " + str(len(ps5_current_store)))
        for ele in ps5_current_store:
            
            storeFindingStatus = ele.text
            is_out_of_stock = storeFindingStatus.find("Out of stock")
            is_not_sold = storeFindingStatus.rfind("Not sold at this store")
            
            # if not sold, don't save it
            # if not out of stock, don't save it
            if is_not_sold == -1 and is_out_of_stock == -1:
                # print(ele)
                # print(is_out_of_stock)
                # print(is_not_sold)
                store_count += 1
                text_file.write("\n-------------\n[Store-%s]\n%s" % (store_count, storeFindingStatus))
                # Sent email now
                build_email_content_found_to(email_to, storeFindingStatus)
                print("Send email with store details")

        if store_count == 0:
            build_email_content_not_found_to(email_to)
            storeFindingStatus = "Nothing to report yet"
            print(storeFindingStatus)
            text_file.write("\n-------------\n%s" % (storeFindingStatus)) 

        text_file.write("\n-------------\n[END::AUTO-GENERATED REPORT]")

    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , "#root div#mainContainer"))
        )
    finally:
        script_end_at = datetime.now()
        elapsed = script_end_at - script_start_at # yields a timedelta object
        print("Script done, took ", elapsed.seconds, " seconds")

    return