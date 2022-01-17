import pytest
from page_object_tests.pages.basket_page import BasketPage
from page_object_tests.pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Bugged link")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # открыть страницу продукта
    page = ProductPage(browser, link)
    page.open()
    # страница продукта открыта
    #page.should_be_product_page()
    # нажать кнопку Добавить в корзину
    page.add_to_basket()
    # посчитать результат математического выражения
    page.solve_quiz_and_get_code()
    # товар добавлен в корзину
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.basket_page_is_empty()
    basket_page.is_present_empty_basket_message()


# негативные проверки

@pytest.mark.xfail(reason="Negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # открыть страницу продукта
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    # нажать кнопку Добавить в корзину
    page.add_to_basket()
    # посчитать результат математического выражения
    page.solve_quiz_and_get_code()
    # отсутствует первое по счету сообщение об успешном добавлении товара в корзину
    page.should_not_be_success_message_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    #отсутствует первое по счету сообщение об успешном добавлении товара в корзину после открытия страницы
    page.should_not_be_success_message_after_opening_of_page()

@pytest.mark.xfail(reason="Negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    # нажать кнопку Добавить в корзину
    page.add_to_basket()
    # посчитать результат математического выражения
    page.solve_quiz_and_get_code()
    # исчезает первое по счету сообщение об успешном добавлении товара в корзину
    page.success_message_should_be_disappeared_after_adding_product_to_basket()

# проверки на то, что гость видит товары, добавленные в корзину, хотя не добовлял их
@pytest.mark.xfail(reason="Negative test")
def test_guest_can_see_product_in_basket_opened_from_product_page_without_product_adding (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.basket_page_is_full()

@pytest.mark.xfail(reason="Negative test")
def test_guest_can_see_empty_basket_message_in_basket_opened_from_product_page_without_product_adding (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.is_not_present_empty_basket_message()
