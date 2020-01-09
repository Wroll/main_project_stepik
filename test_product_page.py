from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import faker

MAIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
REGISTRATION_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# TODO would be better to make prepare_links() method as fixture
def prepare_links():
    xfile = 7
    mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    links = [mask + str(i) for i in range(10) if i != xfile]
    xlink = pytest.param(mask + str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
    links.insert(xfile, xlink)
    return links


@pytest.mark.need_review
@pytest.mark.parametrize('link', prepare_links())
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, MAIN_LINK)
    page.open()
    page.add_to_basket()
    page.should_be_message()
    page.should_be_product_name()
    page.should_be_product_price()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, MAIN_LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, MAIN_LINK)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, MAIN_LINK)
    page.open()
    page.should_be_login_link()


def test_user_cant_see_success_message(browser):
    page = ProductPage(browser, MAIN_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_view_page()
    page.check_items_in_basket()
    page.check_text_in_empty_basket()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = faker.Faker()
        password = faker.Faker()
        registration_page = LoginPage(browser, REGISTRATION_LINK)
        registration_page.open()
        registration_page.register_new_user(email.email(), password.password())
        registration_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, MAIN_LINK)
        page.open()
        page.add_to_basket()
        page.should_be_message()
        page.should_be_product_name()
        page.should_be_product_price()
