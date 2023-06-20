# import required modules
from selenium import webdriver
import random

from data.link import LINK
from data.names import NAMES
from data.surnames import SURNAMES
from data.sessions import SESSIONS


# products = [2085, 2089, 4401, 2087, 2597, 2088]


# Driver Code
if __name__ == "__main__":
    # create object
    browser = webdriver.Edge("msedgedriver.exe")

    browser.get(f"{LINK}")
    # browser.get(f"{LINK}/shop/?add-to-cart={products[0]}")
    browser.delete_all_cookies()
    browser.add_cookie(
        {
            "name": "wp_woocommerce_session_b219c3c5436391f161b53511b65c90f9",
            "value": SESSIONS[random.randint(0, len(SESSIONS) - 1)],
        }
    )
    browser.get(f"{LINK}/finalizar-compra")

    # fill name
    browser.find_element_by_id("billing_first_name").send_keys("hello")

    # click confirm order button
    browser.find_element_by_id("place_order").click()
