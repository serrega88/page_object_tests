from page_object_tests.pages.base_page import BasePage
from page_object_tests.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()

    def should_be_product_url(self):
        current_url = self.browser.current_url
        assert "?promo=" in current_url, "This is not the url of the product page"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def check_product_name_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name == product_name_message, "Wrong product name in the basket"

    def check_product_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == product_price_message, "Wrong product price in the basket"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.FIRST_SUCCESS_MESSAGE), "First success message about the product adding to the basket is presented after adding product to the basket, but should not be"

    def should_not_be_success_message_after_opening_of_page(self):
        assert self.is_not_element_present(*ProductPageLocators.FIRST_SUCCESS_MESSAGE), "First success message about the product adding to the basket is presented after the page opening, but should not be"

    def success_message_should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.FIRST_SUCCESS_MESSAGE), "First success message about the product adding to the basket is not disappiered, but should be"