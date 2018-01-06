import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    import httplib
except:
    import http.client as httplib


TEST_URL = "http://www.python.org"
CONNECTIVITY_CHECK_SECONDS = 10


def main():
    while True:
        # sleep X seconds before next check
        time.sleep(CONNECTIVITY_CHECK_SECONDS)

        # check wifi connectivity
        if not network_alive():
            # toggle wifi setting for osx
            print("Network is dead, turn off and on wifi..")
            os.system("networksetup -setairportpower airport off")
            os.system("networksetup -setairportpower airport on")
            time.sleep(10)

            # check whether the connectivity recovered after toggling wifi
            if not network_alive():
                print("Need re-login, start login process..")
                time.sleep(5)
                login_to_starbucks()
        else:
            print("Network still working, keep productive!")


def network_alive():
    """Check internet connectivity by making a HEAD request to google
    :return:
        bool: indicate network is alive or not
    """
    conn = httplib.HTTPConnection(TEST_URL.replace('http://', ''), timeout=1)
    try:
        # first check we can get response from Google
        conn.request("GET", "/")
        # second check it's not a redirected page
        r1 = conn.getresponse()
        print(r1.status)
        if r1.status not in [301]:
            alive = False
        else:
            alive = True
    except:
        alive = False
    finally:
        conn.close()
        return alive


def login_to_starbucks():
    """
    Open Chrome and login to starbucks for wifi usage
    :return:
    """
    try:
        driver = get_chrome_driver()

        driver.get(TEST_URL)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, 'button_next_page').click()
        driver.implicitly_wait(1)
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