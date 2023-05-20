# importing the necessary modules
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from demo_w_pom.locators import PRODUCT_TITLE, BRAND, STOCK_STATUS_STR, \
    PRODUCT_PRICE, TAX_STR, ADD_TO_CART_BUTTON, SUCCESS_MESSAGE


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.PRODUCT_TITLE = PRODUCT_TITLE
        self.BRAND = BRAND
        self.STOCK_STATUS_STR = STOCK_STATUS_STR
        self.PRODUCT_PRICE = PRODUCT_PRICE
        self.TAX_STR = TAX_STR
        self.ADD_TO_CART_BUTTON = ADD_TO_CART_BUTTON
        self.SUCCESS_MESSAGE = SUCCESS_MESSAGE

    # locating and retrieving the product title
    def get_product_title(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_TITLE))
        product_title = self.driver.find_element(*self.PRODUCT_TITLE)
        return product_title.text

    # locating and retrieving the brand of the product
    def get_product_brand(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BRAND))
        brand = self.driver.find_element(*self.BRAND)
        return brand.text

    # locating and retrieving the stock status of the product
    def get_stock_status(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.STOCK_STATUS_STR))
        stock_status_split = self.driver.find_element(*self.STOCK_STATUS_STR).text.split(':')
        stock_status = stock_status_split[1]
        return stock_status

    # locating and retrieving the product price
    def get_product_price(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_PRICE))
        product_price = self.driver.find_element(*self.PRODUCT_PRICE)
        return product_price.text

    # locating and retrieving the tax
    def get_tax(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TAX_STR))
        tax_split = self.driver.find_element(*self.TAX_STR).text.split(':')
        tax = tax_split[1]
        return tax

    # locating and clicking the add to cart button
    def click_add_to_cart_button(self):
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()

    # checking for success message, which indicates, that addition of MacBook to the cart was successful
    def check_for_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        if success_message.is_displayed():
            print("success message present.")
