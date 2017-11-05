"""
References
- https://stackoverflow.com/questions/37313958/turn-on-off-wifi-with-python-on-osx
"""

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_URL = "http://www.google.com"
CONNECTIVITY_CHECK_SECONDS = 10


def main():
    while True:
        # sleep X seconds before next check
        time.sleep(CONNECTIVITY_CHECK_SECONDS)

        # check wifi connectivity
        if not network_alive:
            # toggle wifi setting for osx
            print("Network is dead, turn off and on wifi..")
            os.system("networksetup -setairportpower airport off")
            os.system("networksetup -setairportpower airport on")

            # check whether the connectivity recovered after toggling wifi
            if not network_alive():
                print("Need re-login, start login process..")
                login_to_starbucks()
        else:
            print("Network still working, keep productive!")


def network_alive():
    """Check internet connectivity by accessing random page
    :return:
        bool: indicate network is alive or not
    """
    res = requests.request(method='GET', url=TEST_URL)
    return True if res.status_code == 200 else False


def login_to_starbucks():
    """
    Open Chrome and login to starbucks for wifi usage
    :return:
    """
    try:
        driver = get_chrome_driver()

        driver.get(TEST_URL)
        driver.find_element(By.ID, 'button_next_page').click()
        driver.find_element(By.ID, 'button_accept').click()
    finally:
        print("Shut down driver..")
        driver.quit()


def get_chrome_driver():
    """Return a selenium driver using Chrome
    """
    return webdriver.Chrome("drivers/chromedriver")


if __name__ == '__main__':
    main()