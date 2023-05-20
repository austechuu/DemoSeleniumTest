# importing necessary modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demo_w_pom.locators import SEARCH_FIELD, SEARCH_BUTTON


class Search:
    def __init__(self, driver):
        self.driver = driver
        self.SEARCH_FIELD = SEARCH_FIELD
        self.SEARCH_BUTTON = SEARCH_BUTTON

    def locate_search_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_FIELD))

    # locating and clicking the search field
    def click_search_field(self):
        search_field = self.locate_search_field()
        search_field.click()

    # locating and entering "MacBook" in the search field
    def enter_search_query(self):
        search_field = self.locate_search_field()
        search_field.send_keys("MacBook")
        return search_field

    # locating and clicking the search_button
    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()
