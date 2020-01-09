from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

# pytest -v --tb=line -m "login_page" --language=en test_main_page.py


LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
LINK_TO_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
MAIN_LINK = "http://selenium1py.pythonanywhere.com"


class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MAIN_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()


def test_correctness_login_form(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_login_form()


def test_correctness_register_form(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_register_form()


def test_correctness_login_url(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, MAIN_LINK)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_view_page()
    page.check_items_in_basket()
    page.check_text_in_empty_basket()
