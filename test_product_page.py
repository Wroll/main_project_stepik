from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import faker

# pytest -v --tb=line --language=en test_product_page.py
LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
# xfile = 7
# mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# links = [mask+str(i) for i in range(10) if i != xfile]
# xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
# links.insert(xfile, xlink)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()


@pytest.mark.from_product_page_to_login_page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.from_product_page_to_login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = faker.Faker()
        password = faker.Faker()
        registration_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        registration_page = LoginPage(browser, registration_link)
        registration_page.open()
        registration_page.register_new_user(email.email(), password.password())
        registration_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, LINK)
        page.open()
        page.add_to_basket()
        page.should_be_message()
        page.should_be_product_name()
        page.should_be_product_price()
