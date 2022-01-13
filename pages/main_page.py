from page_object_tests.pages.base_page import BasePage


class MainPage(BasePage):
    # заглушка в отсутствие методов в классе
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

