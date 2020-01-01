import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

PATH_TO_DRIVER_CHROME = "D:\\drosel\\Driver\\chromedriver.exe"


# 'en,en_US'

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(PATH_TO_DRIVER_CHROME, options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
