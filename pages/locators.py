from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")


class BasketPageLocators:
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1) > a:nth-child(1)")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success>.alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    CLOSE_SUCCESS_MESSAGE_1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > a")
    CLOSE_SUCCESS_MESSAGE_2 = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > a")
