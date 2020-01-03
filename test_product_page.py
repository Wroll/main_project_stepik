from .pages.product_page import ProductPage
import pytest
import time

# pytest -v --tb=line --language=en test_product_page.py
LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"


xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
links = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(xfile, xlink)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    # page.should_be_button()
    # page.should_be_product_page_link()
    page.add_to_basket()
    # page.should_be_message()
    page.should_not_be_success_message()
    page.should_be_success_message()
    page.should_be_product_name()
    page.should_be_product_price()


