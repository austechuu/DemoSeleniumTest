# importing the necessary modules
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the driver pytest fixture
@pytest.fixture
def driver():
    options = Options()
    # setting the driver to run in headless mode
    options.headless = True
    # creating the driver instance
    driver = webdriver.Firefox(options=options)
    # maximizing the window
    driver.maximize_window()
    yield driver
    # quiting the driver after the test is finished
    driver.quit()


class TestECommerce:
    # creating a setup pytest fixture and setting it to autouse=True
    @pytest.fixture(autouse=True)
    def set_up(self, driver):
        self.driver = driver
        self.url = 'http://tutorialsninja.com/demo/'

    def test_demo(self):
        # getting the demo website
        self.driver.get(self.url)

        # locating the search field, clicking on it and entering "MacBook"
        search_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "search")))
        search_field.click()
        search_field.send_keys("MacBook")

        # locating the search button and clicking it
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-default")))
        search_button.click()

        # checking, if the redirect to the search_results page was successful
        assert self.driver.current_url == "https://tutorialsninja.com/demo/index.php?route=product/search&search=MacBook"

        # locating the "MacBook" listing and clicking on it
        macbook_listing = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/a/img")))
        macbook_listing.click()

        # checking if the redirect to the product page was successful
        assert self.driver.current_url == "https://tutorialsninja.com/demo/index.php?route=product/product&product_id=43&search=MacBook"

        # retrieving some values from the product page and storing them in variables
        product_title = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/h1").text
        brand = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[1]/li[1]/a").text
        stock_status_split = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[2]/div/div/div/div[2]/ul[1]/li[4]").text.split(
            ':')
        stock_status = stock_status_split[1]
        product_price = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[2]/li[1]/h2").text
        tax_split = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[2]/li[2]").text.split(
            ":")
        tax = tax_split[1]

        # locating and clicking the add to cart button
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button-cart"]')))
        add_to_cart_button.click()

        # checking if the success message was displayed, indicating, that adding the macbook to cart was successful
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/ html / body / div[2] / div[1]")))
        if success_message.is_displayed():
            print("success message present.")

        # locating and clicking the shopping cart button
        shopping_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[3]/div/button")))
        shopping_cart_button.click()

        # checking if the shopping cart dropdown menu was displayed
        cart_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div[3]/div/ul")))
        if cart_dropdown.is_displayed():
            print("cart dropdown menu present.")

        # locating and clicking the view cart option in the dropdown
        view_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[1]")))
        view_cart.click()

        # checking if the redirect to cart page was successful
        assert self.driver.current_url == "https://tutorialsninja.com/demo/index.php?route=checkout/cart"

        # checking, if the order summary in the cart page is visible
        order_summary = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-offset-8 > table:nth-child(1)")))
        if order_summary.is_displayed():
            print("Order summary is present")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_summary)

        # retrieving some values from the order summary and storing them in variables
        sub_total = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]").text
        eco_tax = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[2]").text
        vat = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]").text
        total = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[4]/td[2]").text

        # locating the checkout button and clicking it
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div[2]/a")))
        checkout_button.click()

        # making dictionaries with the retrieved values from the product page and the order summary
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

        # creating for loops, that iterate through the dictionaries and prints out the key:value pairs
        print("Product page:")
        for key, value in captured_product_values.items():
            print(f"{key}: {value}")

        print("Order summary:")
        for key, value in captured_order_values.items():
            print(f"{key}: {value}")

