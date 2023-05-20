# importing the necessary modules
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from demo_w_pom.locators import SEARCH_RESULTS_URL, PRODUCT_PAGE_URL, CART_URL
from demo_w_pom.search import Search
from demo_w_pom.search_results_page import SearchResultsPage
from demo_w_pom.product_page import ProductPage
from demo_w_pom.cart import Cart


# creating a driver pytest fixture
@pytest.fixture
def driver():
    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


class Test(object):
    # creating a setup pytest fixture and setting it to autouse=True
    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.driver = driver
        self.url = 'http://tutorialsninja.com/demo/'
        self.Search = Search(self.driver)
        self.SearchResultsPage = SearchResultsPage(self.driver)
        self.ProductPage = ProductPage(self.driver)
        self.Cart = Cart(self.driver)

    # writing the test method, which uses the methods from the classes from search.py, search_results.py, product_page.py and cart.py
    def test_ecommerce(self):
        # get url
        self.driver.get(self.url)
        # search
        self.Search.click_search_field()
        self.Search.enter_search_query()
        self.Search.click_search_button()
        # search results page
        assert self.driver.current_url == SEARCH_RESULTS_URL
        self.SearchResultsPage.click_macbook_listing()
        # product page
        assert self.driver.current_url == PRODUCT_PAGE_URL
        product_title = self.ProductPage.get_product_title()
        brand = self.ProductPage.get_product_brand()
        stock_status = self.ProductPage.get_stock_status()
        product_price = self.ProductPage.get_product_price()
        tax = self.ProductPage.get_tax()
        self.ProductPage.click_add_to_cart_button()
        self.ProductPage.check_for_success_message()
        # cart
        self.Cart.click_cart_button()
        self.Cart.check_for_cart_dropdown()
        self.Cart.click_view_cart()
        assert self.driver.current_url == CART_URL
        self.Cart.scroll_to_order_summary()
        sub_total = self.Cart.get_sub_total()
        eco_tax = self.Cart.get_eco_tax()
        vat = self.Cart.get_vat()
        total = self.Cart.get_total()
        self.Cart.click_checkout_button()

        # creating the dictionaries with the retrieved values from the product page and the order summary
        captured_product_values = {
            "product_title": product_title,
            "brand": brand,
            "stock_status": stock_status,
            "product_price": product_price,
            "tax": tax,
        }

        captured_order_values = {
            "sub_total": sub_total,
            "eco_tax": eco_tax,
            "vat": vat,
            "total": total
        }

        # making for loops that iterate through the dictionaries and print the key:value pairs
        print("Product page:")
        for key, value in captured_product_values.items():
            print(f"{key}: {value}")

        print("Order summary:")
        for key, value in captured_order_values.items():
            print(f"{key}: {value}")
