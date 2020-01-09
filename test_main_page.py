from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest
import time

LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
LINK_TO_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()


# pytest -v --tb=line -m "login_page" --language=en test_main_page.py

@pytest.mark.login_page
def test_correctness_login_form(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_login_form()


@pytest.mark.login_page
def test_correctness_register_form(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_register_form()


@pytest.mark.login_page
def test_correctness_login_url(browser):
    page = LoginPage(browser, LINK_TO_LOGIN_PAGE)
    page.open()
    page.should_be_login_url()


@pytest.mark.basket_page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_view_page()
    page.check_items_in_basket()
    page.check_text_in_empty_basket()


@pytest.mark.basket_page
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_view_page()
    page.check_items_in_basket()
    page.check_text_in_empty_basket()
