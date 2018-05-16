import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

try:
    import httplib
except ModeuleNotFouldError:
    import http.client as httplib


TEST_URL = "http://www.google.com"
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
                login_to_starbucks()
        else:
            print("Network still working, keep productive!")


def network_alive():
    """Check internet connectivity by making a HEAD request to google

    Returns
    -------
    bool : indicate network is alive or not
    """
    conn = httplib.HTTPConnection(TEST_URL.replace('http://', ''), timeout=1)
    alive = False
    try:
        # first check we can get response from Google
        conn.request("GET", "/")
        # second check it's not a redirected page
        r1 = conn.getresponse()
        print(r1.status)
        if r1.status not in [302, 200]:
            alive = False
        else:
            alive = True
    except:
        alive = False
    finally:
        conn.close()
        return alive


def login_to_starbucks():
    """Open Chrome and login to starbucks for wifi usage
    """
    delay_seconds = 10
    driver = get_chrome_driver()
    try:
        driver.get(TEST_URL)
        WebDriverWait(driver, delay_seconds).until(EC.presence_of_element_located((By.ID, 'button_next_page')))
        driver.find_element(By.ID, 'button_next_page').click()
        driver.implicitly_wait(1)
        driver.find_element(By.ID, 'button_accept').click()

    except TimeoutException:
        print("Take longer than {} seconds to load page.".format(delay_seconds))

    finally:
        print("Shut down driver..")
        driver.quit()


def get_chrome_driver():
    """Return a selenium driver using Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    return webdriver.Chrome("drivers/chromedriver", chrome_options=options)


if __name__ == '__main__':
    main()