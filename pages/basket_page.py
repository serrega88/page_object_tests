from page_object_tests.pages.base_page import BasePage
from page_object_tests.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "basket" in current_url, "This is not the url of the basket page"

    def basket_page_is_empty(self):
        self.is_not_element_present(*BasketPageLocators.PRODUCTS_BLOCK)

    def is_present_empty_basket_message(self):
        self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
