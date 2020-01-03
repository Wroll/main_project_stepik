from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
LINK_TO_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


# @pytest.mark.main_page
# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


@pytest.mark.main_page
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(5)


@pytest.mark.main_page
def test_guest_should_see_login_link(browser):
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


