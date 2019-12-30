import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec

import time

LINK = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_languages(browser):
    browser.get(LINK)
    time.sleep(5)
    try:
        browser.find_element_by_css_selector("form button.btn.btn-lg")
        b = True
    except NoSuchElementException:
        b = False
    assert b