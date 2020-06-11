from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_the_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_notification_add_to_basket(self):
        assert self.get_text_element(*ProductPageLocators.NAME_PRODUCT_ADD_TO_BASKET) in self.get_product_name(), \
            "Product name in the basket is different from on product page."

    def should_be_basket_price(self):
        assert self.get_text_element(*ProductPageLocators.BASKET_PRICE) in self.get_product_price(), \
            "Product price in the basket is different from on product page."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message is not disappeared but should."

    def get_product_name(self):
        return self.get_text_element(*ProductPageLocators.NAME_PRODUCT)

    def get_product_price(self):
        return self.get_text_element(*ProductPageLocators.PRODUCT_PRICE)
