from selenium.webdriver.common.by import By
from page_object_tests.pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find(By.CSS_SELECTOR, "#login_link")
        login_link.click()