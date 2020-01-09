from .base_page import BasePage
from .locators import ViewBasketLocators, BasePageLocators


class BasketPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BUTTON), "Basket link is not presented"

    def check_items_in_basket(self):
        assert self.is_not_element_present(*ViewBasketLocators.EMPTY_BASKET), "Basket is not empty"

    def check_text_in_empty_basket(self):
        assert self.is_element_present(
            *ViewBasketLocators.TEXT_ABOUT_EMPTY_BASKET), "Text about empty basket not exist"
