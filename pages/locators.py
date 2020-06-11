from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success>.alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")