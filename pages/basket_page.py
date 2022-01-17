from page_object_tests.pages.base_page import BasePage
from page_object_tests.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "basket" in current_url, "This is not the url of the basket page"

    def basket_page_is_full(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_BLOCK), "Basket page is empty, but should be full"

    def basket_page_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BLOCK), "Basket page is full, but should be empty"

    def is_present_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is not an empty basket message, but should be"

    def is_not_present_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is an empty basket message, but should not be"
