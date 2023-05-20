from selenium.webdriver.common.by import By

# search locators
SEARCH_FIELD = (By.NAME, "search")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-default")

# results page locators
SEARCH_RESULTS_URL = 'https://tutorialsninja.com/demo/index.php?route=product/search&search=MacBook'
MACBOOK_LISTING = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/div/div[1]/a/img")

# product page locators
PRODUCT_PAGE_URL = "https://tutorialsninja.com/demo/index.php?route=product/product&product_id=43&search=MacBook"
PRODUCT_TITLE = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/h1")
BRAND = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[1]/li[1]/a")
STOCK_STATUS_STR = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[1]/li[4]")
PRODUCT_PRICE = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[2]/li[1]/h2")
TAX_STR = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/ul[2]/li[2]")
ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')
SUCCESS_MESSAGE = (By.XPATH, "/ html / body / div[2] / div[1]")

# cart related locators
SHOPPING_CART_BUTTON = (By.XPATH, "/html/body/header/div/div/div[3]/div/button")
CART_DROPDOWN = (By.XPATH, "/html/body/header/div/div/div[3]/div/ul")
VIEW_CART = (By.XPATH, "/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[1]")
CART_URL = "https://tutorialsninja.com/demo/index.php?route=checkout/cart"
ORDER_SUMMARY = (By.CSS_SELECTOR, ".col-sm-offset-8 > table:nth-child(1)")
SUB_TOTAL = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]")
ECO_TAX = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[2]")
VAT = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]")
TOTAL = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/table/tbody/tr[4]/td[2]")
CHECKOUT_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div[3]/div[2]/a")
