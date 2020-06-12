from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING), \
            "The basket isn't empty."

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), \
            "The text about empty basket isn't presented"
