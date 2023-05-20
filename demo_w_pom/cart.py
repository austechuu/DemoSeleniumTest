# importing the necessary modules
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from demo_w_pom.locators import SHOPPING_CART_BUTTON, CART_DROPDOWN, VIEW_CART, \
    ORDER_SUMMARY, SUB_TOTAL, ECO_TAX, VAT, TOTAL, CHECKOUT_BUTTON


class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.SHOPPING_CART_BUTTON = SHOPPING_CART_BUTTON
        self.CART_DROPDOWN = CART_DROPDOWN
        self.VIEW_CART = VIEW_CART
        self.ORDER_SUMMARY = ORDER_SUMMARY
        self.SUB_TOTAL = SUB_TOTAL
        self.ECO_TAX = ECO_TAX
        self.VAT = VAT
        self.TOTAL = TOTAL
        self.CHECKOUT_BUTTON = CHECKOUT_BUTTON

    # locating and clicking the cart button
    def click_cart_button(self):
        cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SHOPPING_CART_BUTTON))
        cart_button.click()

    # checking if the cart dropdown menu is present
    def check_for_cart_dropdown(self):
        cart_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CART_DROPDOWN))
        if cart_dropdown.is_displayed():
            print("cart dropdown present.")

    # locating and clicking on the view cart option
    def click_view_cart(self):
        view_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.VIEW_CART))
        view_cart.click()

    # locating the order summary and scrolling it into view by using a JavaScript injection
    def scroll_to_order_summary(self):
        order_summary = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ORDER_SUMMARY))
        if order_summary.is_displayed():
            print("Order summary is present")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_summary)

    # locate and retrieve the subtotal
    def get_sub_total(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUB_TOTAL))
        sub_total = self.driver.find_element(*self.SUB_TOTAL)
        return sub_total.text

    # locate and retrieve eco tax
    def get_eco_tax(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ECO_TAX))
        eco_tax = self.driver.find_element(*self.ECO_TAX)
        return eco_tax.text

    # locate and retrieve vat
    def get_vat(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.VAT))
        vat = self.driver.find_element(*self.VAT)
        return vat.text

    # locate and retrieve total
    def get_total(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TOTAL))
        total = self.driver.find_element(*self.TOTAL)
        return total.text

    # locate and click the checkout button
    def click_checkout_button(self):
        checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_button.click()