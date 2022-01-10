from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_RESET = (By.CSS_SELECTOR, "#login_form p a")
    LOGIN_SUBMIT = (By.NAME, "login_submit")

    REGISTRATION_USERNAME = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    FIRST_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
