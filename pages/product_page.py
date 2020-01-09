from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_product_page_link(self):
        assert "?promo=newYear" in self.browser.current_url, "It's not a product page"

    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button 'throw to basket' not exist"

    def should_be_message(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_SUCCESS_ADDED_INTO_BASKET), \
            "There is no success message about product in the basket"

    def should_be_product_name(self):
        product_name_should_be = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_SHOULD_BE).text
        product_name_added_into_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDED_INTO_BASKET).text
        assert product_name_should_be == product_name_added_into_basket, "Product name is not correct"

    def should_be_product_price(self):
        product_price_should_be = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_SHOULD_BE).text
        product_price_added_into_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_ADDED_INTO_BASKET).text
        assert product_price_should_be == product_price_added_into_basket, "Product price is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"
