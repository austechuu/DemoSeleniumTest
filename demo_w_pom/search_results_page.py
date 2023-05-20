# importing the necessary modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demo_w_pom.locators import MACBOOK_LISTING


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.MACBOOK_LISTING = MACBOOK_LISTING

    # locating and clicking on the MacBook listing
    def click_macbook_listing(self):
        macbook_listing = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MACBOOK_LISTING))
        macbook_listing.click()
